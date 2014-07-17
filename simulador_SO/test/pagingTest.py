from paging import *
from memory import *
from program import *
from pcb import *
from cpu import *
from disk import *

disk = Disk()
mP = Paging(Memory(), 3, disk)
p1 = Program("P1", ['a', 'b', 'c'])
p2 = Program("P2", ['d', 'e'])
p3 = Program("P3", ['f', 'g', 'h', 'i'])
p4 = Program("P4", ['j', 'k', 'l', 'm'])
disk.load("P1", p1)
disk.load("P2", p2)
disk.load("P3", p3)
disk.load("P4", p4)
id4 = id(p4)
pcb4 = PCB(id4, p4.priority, p4.sourceSize())
mP.load(p4, id4)
id3 = id(p3)
pcb3 = PCB(id3, p3.priority, p3.sourceSize())
mP.load(p3, id3)
id2 = id(p2)
pcb2 = PCB(id2, p2.priority, p2.sourceSize())
mP.load(p2, id2)
id1 = id(p1)
pcb1 = PCB(id1, p1.priority, p1.sourceSize())
mP.load(p1, id1)
mP.memoryF.memory.memoryCells
mP.read(pcb4)
pcb4.pc = 3
mP.read(pcb4)
mP.read(pcb3)
mP.read(pcb2)
mP.read(pcb1)


pcb4.pc = 3
cpu = CPU(mP)
cpu.addPcb(pcb4)
cpu.fetch()


