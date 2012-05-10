import time
from snoop.core.processor import Processor

class Slow(Processor):
    def __init__(self, delay=5):
        Processor.__init__(self, 'slow')
        self.delay = delay

    def sample(self):
        doc = {'delay': self.delay}

        # wait a while... maybe a long io operation
        time.sleep(self.delay)

        return doc

