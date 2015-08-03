class MyDict:
    """An unsorted list of key, value pairs"""
    def __init__(self):
        self.keys = []
        self.values = []

    def index(self, key):
        for i, k in enumerate(self.keys):
            if k == key:
                return i
        return None
        
    def get_value(self, key):
        ind = self.index(key)
        try:
            return self.values[ind]
        except TypeError:
            return None
    
    def append(self, key, value):
        ind = self.index(key)
        if ind is None:
            self.keys = self.keys + [key]
            self.values = self.values + [value]
        else:
            self.values[ind] = value

class MySortedDict:
    """A sorted list of key, value pairs"""
    def __init__(self):
        self.keys = []
        self.values = []

    def index(self, key):
        ## binary search
        first = 0
        last = len(self.keys) - 1
        found = False

        while first <= last and not found:
            midpoint = (first + last)/2
            if self.keys[midpoint] == key:
                found = True
            elif item < self.keys[midpoint]:
                last = midpoint + 1
            else:
                first =  midpoint + 1
        return found
        
    def get_value(self, key):
        ind = self.index(key)
        try:
            return self.values[ind]
        except TypeError:
            return None
    
    def append(self, key, value):
        ind = self.index(key)
        if ind is not None:
            self.values[ind] = value
        else:
            keyvals = zip(self.keys, self.values)
            keyvals = sort(keyvals)
            self.keys, self.values = zip(*keyvals)
