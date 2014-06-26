class MemoryManager:
    
    def __init__(self, memory, aStrategy):
        self.memory = memory
        self.allocationList = {}
        self.allocationStrategy = aStrategy

    def load(self, program):
        mAddress = self.allocationStrategy.assignHole(program, self)
        self.memory.load(mAddress, program)
        self.allocationList[mAddress] = program.sourceSize()
    
    def unload(self, mAddress):
        self.allocationList.pop(mAddress)
        self.memory.unload(mAddress, codeSize)
        
    def holeList(self):
            # hole = cantidad de celdas libres.
        orderedList = self.allocationList.items()
        orderedList.sort()
        holes = {}
        for p, r in zip(orderedList[:len(orderedList)-1], orderedList[1:]):
            holeSize = r[1] - (p[0] + p[1])
            if holeSize > 0:
                holes[(p[0] + p[1])] = holeSize
        lastAddress = orderedList[-1][0] + orderedList[-1][1]
        if (lastAddress) < self.memory.size:
            holes[lastAddress] = self.memory.size - lastAddress
        return holes
        
    