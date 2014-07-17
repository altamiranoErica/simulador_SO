class Memory:
    
    def __init__(self, size = 15):
        self.memoryCells = [None for i in range(size)]
        self.size = size
        
    def firstCell(self):
        return 0
        
    def address(self, program):
        return self.memoryCells.index(program[0])
        
    def load(self, address, program):
        print '[memory] load program: %s...' %(program.name)
        for p, r in zip(range(program.sourceSize()), program.source):
            self.loadInstruction(address + p, r)
    
    def loadInstruction(self, address, instruction):
        self.memoryCells[address] = instruction
    
    def unload(self, address, codeSize):
        for i in range(codeSize):
            self.memory.pop(address + i)
    
    def read(self, address):
        print '[memory] read address: %s...' %(address)
        return self.memoryCells[address]
