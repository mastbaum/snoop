from snoop.core.processor import Processor

class Count(Processor):
    '''Counts the number of events processed.'''
    def __init__(self, interval=1000):
        Processor.__init__(self, 'count')
        self.interval = interval
        self.count = 0

    def event(self, event):
        if self.count % self.interval == 0:
            print 'Processing event', self.count
        self.count += 1

    def sample(self):
        doc = {'count': self.count}
        return doc

    def load(self, p):
        self.interval = p.interval
        self.count = p.count

