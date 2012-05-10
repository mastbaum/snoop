from multiprocessing.pool import ThreadPool

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
    def load(self, rhs):
        '''Load data from another instance. Called when instances are replaced
        during a module reload.
        '''
        pass

class ProcessorBlock:
    '''A processor block is analagous to a block of Python statements.  It
    consists of a list of processors, calling each of their `event` methods
    when `event` is called, and each of their `sample` methods when `sample`
    is called.

    There are two ways to create a block of processors: either provide a list
    of `Processor` instances or a list of `(module_name, fromlist)` tuples.
    In the latter case, an instance of every `Processor` found in the given
    modules will be added.
    '''
    def __init__(self, processors):
        self.pool = ThreadPool(processes=2)

        if isinstance(processors[0], Processor):
            self.processors = processors
        else:
            self.processors = []
            self.load_processors(processors)

    def __del__(self):
        self.pool.close()
        self.pool.join()

    def load_processors(self, paths, preserve=True):
        '''(Re)load all processors found in the provided paths and add them to
        this `ProcesorBlock`. If `preserve` is true, load the new instances
        with the data from the old via `Processor.load`, providing some
        rudimentary "schema evolution."
        '''
        import pkgutil
        import inspect
        current_processors = self.processors
        self.processors = []
        for path, fromlist in paths:
            pkg = __import__(path, fromlist=fromlist)
            for importer, name, ispkg in pkgutil.iter_modules(pkg.__path__):
                module = importer.find_module(name).load_module(name)
                for member in inspect.getmembers(module):
                    try:
                        cls = member[1]
                        if issubclass(cls, Processor) and not cls is Processor:
                            print 'Loading Processor', cls
                            new_processor = getattr(module, member[0])()
                            current_processor = filter(lambda x: x.name == new_processor.name, current_processors)
                            if preserve and len(current_processor) > 0:
                                new_processor.load(current_processor[0])
                            self.processors.append(new_processor)
                    except TypeError:
                        pass

    def event(self, ev):
        '''Call `Processor.event(ev)` for each processor'''
        for processor in self.processors:
            processor.event(ev)

    def sample(self):
        '''Call `Processor.sample()` for each processor.
        
        This is done asynchronously with a thread pool farm sampling out to
        multiple cores and prevent I/O-heavy sample methods from blocking
        processing.

        Returns a `multiprocessing.pool.AsyncResult`; `get()` the results out
        when it is `ready()`.
        '''
        return self.pool.map_async(lambda x: (x.name, x.sample()), self.processors)

