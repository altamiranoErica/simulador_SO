from src.paging import *
from src.memory import *
from src.program import *
from src.pcb import *
from src.cpu import *
from src.disk import *

def main():
	disk = Disk()
	p1 = Program("P1", ['a', 'b', 'c'])
	p2 = Program("P2", ['d', 'e'])
	p3 = Program("P3", ['f', 'g', 'h', 'i'])
	p4 = Program("P4", ['j', 'k', 'l', 'm'])

	disk.load("P1", p1)
	disk.load("P2", p2)
	disk.load("P3", p3)
	disk.load("P4", p4)

	id1 = id(p1)
	pcb1 = PCB(id1, p1.priority, p1.sourceSize())
	id2 = id(p2)
	pcb2 = PCB(id2, p2.priority, p2.sourceSize())
	id3 = id(p3)
	pcb3 = PCB(id3, p3.priority, p3.sourceSize())
	id4 = id(p4)
	pcb4 = PCB(id4, p4.priority, p4.sourceSize())

	mP = Paging(Memory(), 3, disk)
	mP.load(p4, id4)
	mP.load(p3, id3)
	mP.load(p2, id2)
	mP.load(p1, id1)
	mI = mP.memoryF.memory.memoryCells[:]

	mP.read(pcb4)
	mP.read(pcb1)
	mP.read(pcb1)
	mF = mP.memoryF.memory.memoryCells

	print 'Inicial memory: %s' %(mI)
	print 'Final memory: %s' %(mF)

if __name__ == "__main__":
    main()
