import time

class Disk:

    def __init__(self):
        self.storage = {}
    
    def load(self, name, program):
        self.storage[name] = program
        
    def read(self, name):
        return self.storage[name]
        
    def delete(self, name):
        self.storage.pop(name)
