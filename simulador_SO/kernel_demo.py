# kernel test

from src.kernel import *
from src.memory import *
from src.program import *
from src.memoryManager import *
from src.allocationStrategy import *
from src.instruction import *

def main():
	mm = ContiguousMemoryAllocation(Memory(), BestFit())
	kernel = FactoryKernel().newKernelWithRoundRobinFifo(mm, 2)

	i1 = CPUInstruction('p1 - i1')
	i2 = CPUInstruction('p1 - i2')
	i3 = CPUInstruction('p1 - i3')
	i4 = CPUInstruction('p1 - i4')
	iIO1 = IOInstruction()
	iIO2 = IOInstruction()

	i5 = CPUInstruction('p2 - i1')
	i6 = CPUInstruction('p2 - i2')
	i7 = CPUInstruction('p2 - i3')
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

