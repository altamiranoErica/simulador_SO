from src.scheduling import *
from src.pcb import *

def main():
	fifo = ReadyQueue()

	pcb1 = PCB(123, 1, 3)
	pcb2 = PCB(234, 1, 5)
	pcb3 = PCB(345, 3, 4)
	pcb4 = PCB(567, 5, 1)

	fifo.addPCB(pcb1)
	fifo.addPCB(pcb2)
	fifo.addPCB(pcb3)
	fifo.addPCB(pcb4)
	print '[Fifo] First PCB: %s' %(fifo.nextPCB().pid)

	priority = Priority(5)

	priority.addPCB(pcb1)
	priority.addPCB(pcb2)
	priority.addPCB(pcb3)
	priority.addPCB(pcb4)
	print '[Priority] First PCB: %s' %(priority.nextPCB().pid)

	pcb5 = PCB(678, 3, 4)
	priority.addPCB(pcb5)
	print '[Priority] First PCB: %s' %(priority.nextPCB().pid)

	pcb6 = PCB(789, 5, 4)
	priority.addPCB(pcb6)
	print '[Priority] First PCB: %s' %(priority.nextPCB().pid)

if __name__ == "__main__":
    main()
