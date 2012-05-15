sample_period = 300
processor_paths = [
    ('processors', ['.']),
]
processor_kwargs = {
    'count': {'interval': 2000},
}
from snoop.writer import PrintWriter
writer = PrintWriter()
from snoop.reader import DispatchReader
reader = DispatchReader('tcp://localhost:5024')

