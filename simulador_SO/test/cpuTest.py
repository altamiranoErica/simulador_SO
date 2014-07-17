from paging import *
from memory import *
from program import *
from pcb import *
from cpu import *
from disk import *
from memoryManager import *
from allocationStrategy import *
from instruction import *

def command():
	print 'Command'


iE = ExecutableInstruction(command)
iIO = IOInstruction('Mouse')

cMA = ContiguousMemoryAllocation(Memory(), FirstFit())
disk = Disk()
p1 = Program("P1", [iE, iE, iIO])
disk.load("P1", p1)
id1 = id(p1)
pcb1 = PCB(id1, p1.priority, p1.sourceSize())
cMA.load(p1, id1)

cpu = CPU(cMA)
cpu.addPcb(pcb1)
cpu.fetch()
