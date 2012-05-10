# configuration for snoop

# sample period in seconds
sample_period = 5

# python paths to snoop processors as (name, fromlist) tuples, e.g.
#     [ ('full.module.path', ['full.module']) ]
processor_paths = [
    ('snoop.processors', ['snoop'])
]

# keyword arguments to provide to new processor subclass instances
processor_kwargs = {
    'count': {'interval': 2000},
    'exception': {'fail_after': '250'},
    'slow': {'delay': '2'}
}

# Writer to handle output
from snoop.core.writer import PrintWriter
writer = PrintWriter()

# Reader from which to get events
from snoop.core.reader import AirfillReader
reader = AirfillReader('/home/mastbaum/snoop/file.root')

