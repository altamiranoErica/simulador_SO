from interruptHandler import *
from instruction import *
import paging

class CPU:

    def __init__(self, mManager, clock):
        self.memoryManager = mManager
        self.pcb = None
        clock.addObserver(self)
        
    def addPcb(self, pcb):
        print '[cpu] add pcb: %s... ' %(pcb.pid)
        self.pcb = pcb    
    
    def execute(self, instruction):
        if self.pcb.pc > self.pcb.programSize:
            print '[cpu] finished process... '
            instance_InterruptHandler().interrupt(InterruptHandler.KILL)
        elif instruction.iType == Instruction.CPU:
            print '[cpu] running instruction... '
            print instruction.command()
        elif instruction.iType == Instruction.IO:
            print '[cpu] waiting IO...'
            instance_InterruptHandler().interrupt(InterruptHandler.WAIT_IO)
        
    def fetch(self):
        try:
            instruction = self.memoryManager.read(self.pcb)
        except paging.PageFault as exception:
            print exception
            instruction = self.memoryManager.read(self.pcb)
        finally:
            self.pcb.incrementPc()
            self.execute(instruction)
        
    def notify(self):
        if self.pcb is not None:
            self.fetch()
        
    def takePcb(self):
        print '[cpu] take current pcb: %s... ' %(self.pcb.pid)
        currentPcb = self.pcb
        self.pcb = None
        return currentPcb
