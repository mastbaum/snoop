class ProcessorAbort(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class Processor:
    def __init__(self, name):
        self.name = name
    def event(self, event):
        return None
    def write(self, doc={}):
        return doc

class ProcessorBlock:
    def __init__(self, processors=[]):
        self.processors = processors
    def event(self, ev):
        for processor in self.processors:
            processor.event(ev)
    def write(self, doc={}):
        for processor in self.processors:
            doc = processor.write(doc)
        return doc

