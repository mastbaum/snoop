import sys
import time

import config

from snoop.core.processor import ProcessorBlock
from snoop.core.reader import AirfillReader
from snoop.core.writer import PrintWriter

from snoop.processors import NHITStatistics
from snoop.processors import Slow

ts_now = lambda: int(time.time()/60)

processor_block = ProcessorBlock([
    Slow(delay=10),
    NHITStatistics()
])

writer = PrintWriter()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'Usage:', sys.argv[0], '[filename]'
        sys.exit(1)

    reader = AirfillReader(sys.argv[1])    
    events = reader.read()

    results = []
    start_time = time.time()
    sample_count = 0

    # event loop
    while True:
        # write available sample results
        for result in results:
            if result.ready():
                writer.write(result.get(), timestamp=ts_now())
                results.remove(result)

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
            time.sleep(10e-06)
            continue

