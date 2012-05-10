import urllib2
import time
from snoop.core.processor import Processor

class Slow(Processor):
    def __init__(self, delay=5):
        Processor.__init__(self, 'slow')
        self.delay = delay
        self.foo = 0

    def event(self, event):
        self.foo += 1

    def sample(self):
        print 'sample slow'
        doc = {'delay': self.delay, 'foo': self.foo}
        time.sleep(self.delay)
        p = urllib2.urlopen('http://www.google.com')
        doc['google'] = p.read()[:20]
        return doc

