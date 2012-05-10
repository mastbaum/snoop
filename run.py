import sys
import time
import config
from snoop.core.processor import ProcessorBlock

# timestamp by minute
ts_now = lambda: int(time.time()/60)

def write_results(results):
    for result in results:
        if result.ready():
            config.writer.write(result.get(), timestamp=ts_now())
            results.remove(result)

def main():
    # build the processor block
    processor_block = ProcessorBlock(config.processor_paths)

    events = config.reader.read()

    results = []
    start_time = time.time()
    sample_count = 0

    # event loop
    while True:
        # write available sample results
        write_results(results)

        # sample with specified period
        if time.time() - start_time > sample_count * config.sample_period:
            sample_count += 1
            result = processor_block.sample()
            results.append(result)

        # process an event
        try:
            event = events.next()
            processor_block.event(event)
        except StopIteration:
            result = processor_block.sample()
            results.append(result)
            break

    # wait for any remaining samples to complete
    while len(results) > 0:
        write_results(results)
        time.sleep(0.1)

if __name__ == '__main__':
    main()

