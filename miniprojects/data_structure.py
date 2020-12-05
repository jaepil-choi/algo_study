from collections.abc import MutableSequence

class FixedArray(MutableSequence):
    def __init__(self, length, ):
        self.array = [None] * length
        super().__init__()
        
    def __getitem__(self, key):
        return self.array[key]
    
    def __len__(self):
        return len(self.array)

    def __delitem__(self, key):
        del(self.array[key])
        return 
    
    def __setitem__(self, key, item):
        self.array[key] = item
        return
    
    def insert(self, key, item):
        self.array[key:key] = [item]
        return