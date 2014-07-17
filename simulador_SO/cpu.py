from interruptHandler import *
from instruction import *
import paging

class CPU:

    def __init__(self, mManager, clock):
        self.memoryManager = mManager
        clock.addObserver(self)
        
    def addPcb(self, pcb):
        self.pcb = pcb    
    
    def execute(self, instruction):
        if self.pcb.pc > self.pcb.programSize:
            instance_InterruptHandler().interrupt(InterruptHandler.KILL)
        elif instruction.iType == Instruction.EXECUTABLE:
            print 'Running instruction... '
            instruction.command()
        elif instruction.iType == Instruction.IO:
            print 'Waiting for %s' %(instruction.resource)
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
        self.fetch()
        
    def takePcb(self):
        currentPcb = self.pcb
        self.pcb = None
        return currentPcb
