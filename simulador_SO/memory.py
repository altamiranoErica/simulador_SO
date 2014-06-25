class Memory:
    
    def __init__(self, size = 100):
        self.memoryCells = []
        self.size = size
        
    def address(self, program):
        return self.memoryCells.index(program[0])
        
    def load(self, address, program):
        for p, r in zip(range(program.sourceSize), program.source):
            self.memoryCells.insert(address + p, r)
    
    def unload(self, address, codeSize):
        for i in range(codeSize):
            self.memory.pop(address + i)
    
    def read(self, address):
        return self.memoryCells[address]
