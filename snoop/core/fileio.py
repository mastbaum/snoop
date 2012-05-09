from rat import dsreader, ROOT

# normal dsreader imported into local namespace from rat

def tree_reader(filename, tree, branch, obj):
    '''Read events from a ROOT tree'''
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
    yield tree_reader(filename, 'PackT', 'PackRec', rec)

def airfill_dsreader(filename):
    '''Read events from an air-fill style packed ROOT file

    Returns an iterator over the PackedEvent objects in the `PackEv` tree in
    file `filename`.
    '''
    rec = ROOT.RAT.DS.PackedEvent()
    yield tree_reader(filename, 'PackT', 'PackEv', rec)

