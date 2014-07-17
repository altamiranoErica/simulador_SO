from src.memoryManager import *
from src.memory import *
from src.program import *
from src.allocationStrategy import *
from src.pcb import *

def main():
	memory = Memory()
	cMA = ContiguousMemoryAllocation(memory, FirstFit())
	p1 = Program("P1", ['a', 'b', 'c'])
	p2 = Program("P2", ['d', 'e'])
	p3 = Program("P3", ['f', 'g', 'h', 'i'])
	p4 = Program("P4", ['j', 'k', 'l', 'm'])

	id1 = id(p1)
	pcb1 = PCB(id1, p1.priority, p1.sourceSize())
	id2 = id(p2)
	pcb2 = PCB(id2, p2.priority, p2.sourceSize())
	id3 = id(p3)
	pcb3 = PCB(id3, p3.priority, p3.sourceSize())
	id4 = id(p4)
	pcb4 = PCB(id4, p4.priority, p4.sourceSize())

	cMA.load(p1, id1)
	cMA.load(p2, id2)
	cMA.load(p3, id3)
	cMA.load(p4, id4)

	print 'Inicial holes: %s' %(cMA.holeList())
	cMA.unload(id2)
	print 'Holes after that unload "P2": %s' %(cMA.holeList())
	cMA.unload(id3)
	print 'Holes after that unload "P3": %s' %(cMA.holeList())
	cMA.compact()
	print 'Holes after that compact memory: %s' %(cMA.holeList())
	print 'Memory state: %s' %(cMA.memory.memoryCells)

if __name__ == "__main__":
    main()
