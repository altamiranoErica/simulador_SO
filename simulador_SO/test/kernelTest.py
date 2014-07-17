# kernel test

from src.kernel import Kernel

def main():
	mm = ContiguousMemoryAllocation(Memory(), BestFit())
	rq = ReadyQueue()

	kernel = Kernel(mm, rq)

	rr = RoundRobin(rq, 2, kernel.clock, kernel.cpu)
	kernel.shortScheduler = rr

	i1 = CPUInstructionPrintString('p1 - i1')
	i2 = CPUInstructionPrintString('p1 - i2')
	i3 = CPUInstructionPrintAdd(1, 2)
	i4 = CPUInstructionPrintAdd(3, 4)
	iIO1 = IOInstruction()
	iIO2 = IOInstruction()

	i5 = CPUInstructionPrintString('p2 - i1')
	i6 = CPUInstructionPrintString('p2 - i2')
	i7 = CPUInstructionPrintAdd(9, 0)
	iIO3 = IOInstruction()

	p1 = Program("P1", [i1, i2, i3, i4, iIO1, iIO2])
	p2 = Program("P2", [i5, i6, iIO3])

	kernel.startUp()
	kernel.loadProgramToDisk(p1)
	kernel.loadProgramToDisk(p2)

	kernel.runProgram("P2")
	kernel.runProgram("P1")

if __name__ == "__main__":
    main()

