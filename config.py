# configuration for snoop

# sample period in seconds
sample_period = 5

# python paths to snoop processors as (name, fromlist) tuples, e.g.
#     [ ('full.module.path', ['full.module']) ]
processor_paths = [
    ('snoop.processors', ['snoop'])
]

# Writer to handle output
from snoop.core.writer import PrintWriter
writer = PrintWriter()

# Reader from which to get events
from snoop.core.reader import AirfillReader
reader = AirfillReader('file.root')

