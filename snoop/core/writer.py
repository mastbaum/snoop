class Writer:
    '''Output handler'''
    def __init__(self):
        pass
    def write(self, name, timestamp, sample_function):
        pass

class PrintWriter(Writer):
    '''Output handler that just prints'''
    def __init__(self):
        Writer.__init__(self)
    def write(self, name, timestamp, sample_function):
        key = '_'.join(map(str, [name, timestamp]))
        print key, sample_function()

class CouchDBWriter(Writer):
    '''Output handler that writes to a CouchDB database'''
    def __init__(self, host, dbname, username=None, password=None):
        Writer.__init__(self)
        import couchdb
        couch = couchdb.Server(host)
        couch.resource.credentials = (username, password)
        self.db = couch[dbname]
    def write(self, name, timestamp, sample_function):
        doc = sample_function()
        doc['_id'] = '_'.join(map(str, [name, timestamp]))
        if 'timestamp' not in doc:
            doc['timestamp'] = timestamp
        self.db.save(doc)

