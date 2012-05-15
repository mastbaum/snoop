class ROOTFileReader:
    '''Read entries from a ROOT tree in a file.'''
    def __init__(self, filenames, tree_name, branch_name, obj):
        if not hasattr(filenames, '__iter__'):
            filenames = [filenames]
        self.filenames = filenames

        self.tree_name = tree_name
        self.branch_name = branch_name
        self.obj = obj
        self.event_count = 0

    def load_tree(self):
        '''Load the ROOT tree for reading. This is deferred until the first
        read to prevent file descriptors from getting lost if running as a
        daemon.
        '''
        import ROOT
        self.tree = ROOT.TChain(self.tree_name)
        for filename in self.filenames:
            self.tree.Add(filename)

        self.tree.SetBranchAddress(self.branch_name, self.obj)
        self.total_events = self.tree.GetEntries()

    def read(self):
        '''Generator of entries on the requested branch. Raises `StopIteration`
        when no more entries are available.
        '''
        if not hasattr(self, 'tree'):
            self.load_tree()

        while self.event_count < self.total_events:
            self.tree.GetEntry(self.event_count)
            yield self.obj
            self.event_count += 1

class DispatchReader:
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
        self.client.add_db(host, dbname, mapper)

    def read(self):
        '''Generator of events from the dispatcher.'''
        while True:
            yield self.client.recv()

