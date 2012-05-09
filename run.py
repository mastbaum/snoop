import sys
from snoop.core import airfill_dsreader
from snoop.core import ProcessorBlock
from snoop.core import PrintWriter
from snoop.analysis import NHITStatistics

processors = [NHITStatistics()]
processor_block = ProcessorBlock(processors)

writer = PrintWriter()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'Usage:', sys.argv[0], '[filename]'
        sys.exit(1)

    for event in airfill_dsreader(sys.argv[1]):
        processor_block.event(event)

    processor_block.sample(writer)

