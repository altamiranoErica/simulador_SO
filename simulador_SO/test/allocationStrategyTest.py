from memoryManager import *
from memory import *
from allocationStrategy import *

m = MemoryPool(0, 3)
m2 = MemoryPool(10, 4)
m1 = MemoryPool(6, 2)
cMA = ContiguousMemoryAllocation(Memory(), FirstFit())
cMA.allocationList[id(m)] = m
cMA.allocationList[id(m1)] = m1
cMA.allocationList[id(m2)] = m2
ff = FirstFit()
a = ff.assignHole(1, cMA)
a
bf = BestFit()
b = bf.assignHole(1, cMA)
b
wf = WorstFit()
c = wf.assignHole(1, cMA)
c

