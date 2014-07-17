class MemoryManager:
    
    def load(self, program, idPcb):
        raise NotImplementedError
        
    def read(self, pcb):
        raise NotImplementedError
        
    def unload(self, idPcb):
        raise NotImplementedError
        
    def verifyMemorySpace(self, size):
        raise NotImplementedError


class ContiguousMemoryAllocation(MemoryManager):
    
    def __init__(self, memory, aStrategy):
        self.memory = memory
        self.allocationList = []
        self.allocationStrategy = aStrategy
        
    def verifyMemorySpace(self, size):
        holes = filter(lambda t: t[1] >= size, self.holeList().items())
        if len(holes) > 0:
            return True
        self.compact()
        return self.holeList()[0][1] >= size
        
    def load(self, program, idPcb):
        mAddress = self.getAddress(program.sourceSize())
        self.memory.load(mAddress, program)
        mPool = MemoryPool(idPcb, mAddress, program.sourceSize())
        self.allocationList.append(mPool)
        
    def getAddress(self, programSize):
        if len(self.allocationList) == 0:
            return self.memory.firstCell()
        else:
            return self.allocationStrategy.assignHole(programSize, self)
    
    def unload(self, idPcb):
        mPool = [mp for mp in self.allocationList if mp.idPcb == idPcb][0]
        self.allocationList.remove(mPool)
        
    def read(self, pcb):
        mPool = [mp for mp in self.allocationList if mp.idPcb == pcb.pid][0]
        return self.memory.read(mPool.memoryAddress + pcb.pc)
        
    def holeList(self):
        # hole = cantidad de celdas libres.
        if len(self.allocationList) == 0:
            return {self.memory.firstCell(): self.memory.size}
        orderedList = self.allocationList
        orderedList.sort(key=lambda mp: mp.memoryAddress)
        return self.holesIfMemoryIsUsed(orderedList)
        
    def holesIfMemoryIsUsed(self, orderedList):
        holes = {}
        if orderedList[0].memoryAddress > 0:
            holes[0] = orderedList[0].memoryAddress
        for p, r in zip(orderedList[:len(orderedList)-1], orderedList[1:]):
            holeSize = r.memoryAddress - (p.memoryAddress + p.size)
            if holeSize > 0:
                holes[(p.memoryAddress + p.size)] = holeSize
        lastAddress = orderedList[-1].memoryAddress + orderedList[-1].size
        if (lastAddress) < self.memory.size:
            holes[lastAddress] = self.memory.size - lastAddress
        return holes
        
    def compact(self):
        mPools = self.allocationList
        mPools.sort(key=lambda mp: mp.memoryAddress)
        for p, r in zip(mPools[:len(mPools)-1], mPools[1:]):
            newAddress = p.memoryAddress + p.size
            for i in range(r.size):
                instruction = self.memory.read(r.memoryAddress + i)
                self.memory.loadInstruction(newAddress + i, instruction)
            r.memoryAddress = newAddress
                

class MemoryPool:
    
    def __init__(self, idPcb, mAddress, sourceSize):
        self.idPcb = idPcb
        self.memoryAddress = mAddress
        self.size = sourceSize
