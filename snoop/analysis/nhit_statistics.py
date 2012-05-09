from rat import ROOT
from snoop.core import Processor, ProcessorAbort

class NHITStatistics(Processor):
    def __init__(self):
        Processor.__init__(self, 'NHITStatistics')
        self.count = 0
        self.mean_nhit = 0.0
        self.count_lt_30 = 0
        self.count_gte_30 = 0

    def event(self, event):
        if isinstance(event, ROOT.RAT.DS.PackedEvent):
            nhit = event.NHits
        elif isinstance(event, ROOT.RAT.DS.EV):
            nhit = event.GetNhits()
        else:
            raise ProcessorAbort('unknown event type')

        self.count += 1

        self.mean_nhit = self.mean_nhit + (nhit - self.mean_nhit) / self.count

        if nhit < 30:
            self.count_lt_30 += 1
        else:
            self.count_gte_30 += 1

    def write(self, doc={}):
        d = doc.get('nhit_statistics', {})
        d.setdefault('mean', self.mean_nhit)
        d.setdefault('count_lt_30', self.count_lt_30)
        d.setdefault('count_gte_30', self.count_gte_30)
        doc.setdefault('nhit_statistics', d)
        return doc

    def flush(self, doc={}):
        self.write(self, doc)
        self.__init__(self)

