from rat import dsreader, ROOT

# normal dsreader imported into local namespace from rat

def tree_reader(filename, tree, branch, obj):
    '''Read data from the branch named `branch` of a ROOT tree named `tree`
    in a file `filename`. `obj` is a "reference" to an object of the type
    stored in the tree (cf. `SetBranchAddress(branch, &obj)`).
    '''
    tree = ROOT.TChain(tree)
    tree.Add(filename)
    tree.SetBranchAddress(branch, obj)
    total_events = tree.GetEntries()
    event_count = 0

    while event_count < total_events:
        tree.GetEntry(event_count)
        yield obj
        event_count += 1

def packed_dsreader(filename):
    '''Read events from a packed ROOT file

    Returns an iterator over the PackedRec objects in the `PackT` tree in file
    `filename`.
    '''
    rec = ROOT.RAT.DS.PackedRec()
    for o in tree_reader(filename, 'PackT', 'PackRec', rec):
        yield o

def airfill_dsreader(filename):
    '''Read events from an air-fill style packed ROOT file

    Returns an iterator over the PackedEvent objects in the `PackEv` tree in
    file `filename`.
    '''
    rec = ROOT.RAT.DS.PackedEvent()
    for o in tree_reader(filename, 'PackT', 'PackEv', rec):
        yield o

