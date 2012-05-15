from snoop.processor import Processor

class Count(Processor):
    '''Counts the number of events processed.'''
    name = 'count'
    def __init__(self, interval=1000):
        Processor.__init__(self)
        self.interval = interval
        self.count = 0

    def event(self, event):
        '''This is called once per event.'''
        if self.count % self.interval == 0:
            print 'Processing event', self.count

        if event:
            self.count += 1

    def sample(self):
        '''This is called on a fixed timer, and should return a dictionary
        that represents the state of the processor.
        '''
        doc = {'count': self.count, 'interval': self.interval}
        return doc

    def load(self, p):
        '''This is called when processors are reloaded, with the old processor
        instance as `p`. It is used to save state on processor reload.
        '''
        self.interval = p.interval
        self.count = p.count

