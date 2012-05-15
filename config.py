# configuration for snoop

# sample period in seconds
sample_period = 300

# python paths to snoop processors as (name, fromlist) tuples, e.g.
#     [ ('full.module.path', ['full.module']) ]
processor_paths = [
    ('processors', ['.']),
]

# keyword arguments to provide to new processor subclass instances
processor_kwargs = {
    'count': {'interval': 2000},
}

# Writer to handle output
from snoop.writer import PrintWriter
writer = PrintWriter()

# Reader from which to get events
from snoop.reader import DispatchReader
reader = DispatchReader('tcp://localhost:5024')

