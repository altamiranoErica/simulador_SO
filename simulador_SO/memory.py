class Memory:
    
    def __init__(self):
        self.memoryCells = []
        
    def load(self, program):
        self.memoryCells.append(program)
        return self.memoryCells.index(program)
    
    def unload(self, address):
        self.memory.pop(address)
    
    def read(self, address):
        return self.memoryCells[address]
