# dummy configuration for snoop, for sphinx
sample_period = 5
processor_paths = [
    ('snoop.processors', ['snoop'])
]
from snoop.writer import PrintWriter
writer = PrintWriter()
from snoop.reader import AirfillReader
reader = AirfillReader('foo')

