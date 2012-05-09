from multiprocessing.pool import ThreadPool
import time

class ProcessorAbort(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class Processor:
    '''A Processor represents a chunk of analysis code that can be placed into
    the event loop by the user.
    '''
    def __init__(self, name):
        self.name = name
    def event(self, event):
        '''Called once per event.'''
        pass
    def sample(self):
        '''Called periodically, "sampling" the processor state.'''
        return {}

class ProcessorBlock:
    '''A processor block is analagous to a block of Python statements.  It
    consists of a list of processors, calling each of their `event` methods
    when `event` is called, and each of their `sample` methods when `sample`
    is called.
    '''
    def __init__(self, processors=[]):
        self.processors = processors
        self.pool = ThreadPool(processes=2)
    def event(self, ev):
        '''Call `Processor.event(ev)` for each processor'''
        for processor in self.processors:
            processor.event(ev)
    def sample(self, writer, timestamp=int(time.time()/60), doc={}):
        '''Sample all processors through `Writer` `writer`.
        
        `writer` is run with each processor's `sample` method, farming out
        both the sampling and writing to multiple threads (preventing I/O-heavy
        `sample` methods from blocking processing).
        '''
        self.pool.map_async(lambda x: writer.write(*x), [(processor.name, timestamp, processor.sample) for processor in self.processors])

