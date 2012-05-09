from rat import ROOT

class FileReader:
    '''Read entries from a ROOT tree in a file.'''
    def __init__(self, filenames, tree_name, branch_name, obj):
        if not hasattr(filenames, '__iter__'):
            filenames = [filenames]

        self.obj = obj

        self.tree = ROOT.TChain(tree_name)
        for filename in filenames:
            self.tree.Add(filename)

        self.tree.SetBranchAddress(branch_name, obj)
        self.total_events = self.tree.GetEntries()
        self.event_count = 0

    def read(self):
        '''Generator of entries on the requested branch. Raises `StopIteration`
        when no more entries are available.
        '''
        while self.event_count < self.total_events:
            self.tree.GetEntry(self.event_count)
            yield self.obj
            self.event_count += 1

class PackedReader(FileReader):
    '''Read packed records from the `PackRec` branch of the `PackT` tree in a
    packed ROOT file.
    '''
    def __init__(self, filenames):
        tree_name = 'PackT'
        branch_name = 'PackRec'
        obj = ROOT.RAT.DS.PackedRec()
        FileReader.__init__(self, filenames, tree_name, branch_name, obj)

class AirfillReader(FileReader):
    '''Read packed events from the `PackEv` branch of the `PackT` tree in an
    air fill-format packed ROOT file.
    '''
    def __init__(self, filenames):
        tree_name = 'PackT'
        branch_name = 'PackEv'
        obj = ROOT.RAT.DS.PackedEvent()
        FileReader.__init__(self, filenames, tree_name, branch_name, obj)

class RATReader(FileReader):
    '''Read RAT DSes from the `ds` branch of the `T` tree in a normal
    (unpacked) RAT ROOT file.
    '''
    def __init__(self, filenames):
        tree_name = 'T'
        branch_name = 'ds'
        obj = ROOT.RAT.DS.Root()
        FileReader.__init__(self, filenames, tree_name, branch_name, obj)

class DispachReader:
    '''Read records from the dispatcher stream at `address`.'''
    def __init__(self, address):
        import avalanche
        self.address = address
        self.client = avalanche.Client()
        self.client.add_dispatcher(address)

    def add_dispatcher(self, address):
        '''Attach an additional dispatch stream to this reader. See `avalanche`
        documentation for more details.
        '''
        self.client.add_dispatcher(address)

    def add_db(self, host, dbname, mapper):
        '''Attach a database changes feed to this reader. See `avalanche`
        documentation for more details.'''
        self.client.add_dispatcher(host, dbname, mapper)

    def read(self):
        '''Generator of events from the dispatcher.'''
        while True:
            yield self.client.recv()
