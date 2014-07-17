from memoryManager import *
from memory import *
from allocationStrategy import *

def main():
	m = MemoryPool('pcb1', 0, 3)
	m2 = MemoryPool('pcb2', 10, 4)
	m1 = MemoryPool('pcb3', 6, 2)
	
	cMA = ContiguousMemoryAllocation(Memory(), FirstFit())
	cMA.allocationList = [m, m1, m2]

	holes = cMA.holeList()
	ff = FirstFit().assignHole(1, cMA)
	bf = BestFit().assignHole(1, cMA)
	wf = WorstFit().assignHole(1, cMA)

	print 'Hole list: %s' %(holes)
	print '[FirstFit] allocation: %s' %(ff)
	print '[BestFit] allocation: %s' %(bf)
	print '[WorstFit] allocation: %s' %(wf)

if __name__ == "__main__":
    main()
