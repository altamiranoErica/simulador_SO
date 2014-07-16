class MemoryManager:
    
    def load(self, program):
        raise NotImplementedError
        
    def read(self, pcb):
        raise NotImplementedError


class ContiguousMemoryAllocation(MemoryManager):
    
    def __init__(self, memory, aStrategy):
        self.memory = memory
        self.allocationList = []
        self.allocationStrategy = aStrategy

    def load(self, program):
        mAddress = self.getAddress(program.sourceSize())
        self.memory.load(mAddress, program)
        mPool = MemoryPool(mAddress, program.sourceSize())
        self.allocationList.append(mPool)
        return mPool.poolId
        
    def getAddress(self, programSize):
        if len(self.allocationList) == 0:
            return self.memory.firstCell()
        else:
            return self.allocationStrategy.assignHole(programSize, self)
    
    def unload(self, mAddress):
        mPool = [mp for mp in self.allocationList if mp.memoryAddress == mAddress][0]
        self.allocationList.remove(mPool)
        #self.memory.unload(mAddress, codeSize)
        
    def read(self, pcb):
        mPool = [mp for mp in self.allocationList if mp.poolId == pcb.memoryAddress][0]
        return self.memory.read(mPool.memoryAddress + pcb.pc)
        
    def holeList(self):
        # hole = cantidad de celdas libres.
        orderedList = self.allocationList
        orderedList.sort(key=lambda mp: mp.memoryAddress)
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
    
    def __init__(self, mAddress, sourceSize):
        self.poolId = id(self)
        self.memoryAddress = mAddress
        self.size = sourceSize
    
'''class Pagination(MemoryManager):
    
    def load(self, program):
    
    def read(self, pcb):'''
