from memoryManager import *
from memory import *
from program import *
from allocationStrategy import *
from pcb import *

memory = Memory()
cMA = ContiguousMemoryAllocation(memory, FirstFit())
p1 = Program("P1", ['a', 'b', 'c'])
p2 = Program("P2", ['d', 'e'])
p3 = Program("P1", ['f', 'g', 'h', 'i'])
aM1 = cMA.load(p1)
aM2 = cMA.load(p2)
aM3 = cMA.load(p3)
cMA.memory.memoryCells

pcb1 = newPcb = PCB(id(p1), aM1, 1)
pcb2 = newPcb = PCB(id(p2), aM2, 1)
pcb3 = newPcb = PCB(id(p3), aM3, 1)
cMA.read(pcb1)

cMA.unload(cMA.allocationList[1].memoryAddress)
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

