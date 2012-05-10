# dummy configuration for snoop, for sphinx
sample_period = 5
processor_paths = [
    ('snoop.processors', ['snoop'])
]
from snoop.core.writer import PrintWriter
writer = PrintWriter()
from snoop.core.reader import AirfillReader
reader = AirfillReader('foo')

