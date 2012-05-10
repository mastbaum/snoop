from snoop.core.processor import Processor

class ExceptionMaker(Processor):
    '''Raise an exception after a few events. Intended for testing of
    exception handling in the event loop.
    '''
    def __init__(self, fail_after=100):
        Processor.__init__(self, 'exception_maker')
        self.fail_after = fail_after
        self.count = 0
    def event(self, ev):
        self.count += 1
        if self.count < self.fail_after:
            raise Exception('''I'm exceptional!''')
    def sample(self):
        doc = {
            'count': self.count
        }

        return doc

