from memoryManager import *
from memory import *
from program import *
from allocationStrategy import *

memory = Memory()
cMA = ContiguousMemoryAllocation(memory, FirstFit())
p1 = Program("P1", ['a', 'b', 'c'])
p2 = Program("P2", ['d', 'e'])
p3 = Program("P1", ['f', 'g', 'h', 'i'])
cMA.load(p1)
cMA.load(p2)
cMA.load(p3)
cMA.memory.memoryCells
cMA.holeList()
keys = cMA.allocationList.keys()
cMA.unload(keys[1])
cMA.memory.memoryCells
cMA.holeList()
cMA.load(p1)
cMA.memory.memoryCells
cMA.holeList()
cMA.compact()
cMA.holeList()
cMA.memory.memoryCells

'''keys = cMA.allocationList.keys()
cMA.unload(keys[1])
cMA.load(p1)
cMA.unload(keys[2])
cMA.load(p2)
cMA.memory.memoryCells
cMA.compact()'''

