import time

class Disk:

    def __init__(self):
        self.storage = {}
    
    def load(self, name, program):
        print('[disk] loading program %s...') %(name)
        self.storage[name] = program
        
    def read(self, name):
        print('[disk] read %s...') %(name)
        return self.storage[name]
        
    def delete(self, name):
        self.storage.pop(name)
        
    def containsName(self, name):
        return name in self.storage.keys()
