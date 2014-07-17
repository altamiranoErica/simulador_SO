# modulo interruptionCommands:
#   implementa las rutinas que corresponden a cada tipo de interrupcion.
from interruptHandler import *
from pcb import *

class InterruptCommand:
    
    def iType(self):
        raise NotImplementedError
    
    def execute(self, iHandler):
        self.cpu = iHandler.cpu
        self.rQueue = iHandler.readyQueue
        self.executeCommand(iHandler)
        
    def executeCommand(self, iHandler):
        raise NotImplementedError
        
    def addPCBtoReadyQueue(self, pcb):
        if self.rQueue.isEmpty():
            self.cpu.addPcb(pcb)
        else:
            self.rQueue.addPCB(pcb)
            
    def addNewPCBToCPU(self):
        if not self.rQueue.isEmpty():
            self.cpu.add(iHandler.queue.nextPCB())

    
class NewCommand(InterruptCommand):
    
    def iType(self):
        return InterruptHandler.NEW
    
    def addProgramName(self, pName):
        self.programName = pName
    
    def executeCommand(self, iHandler):
        program = iHandler.disk.read(self.programName)
        idPcb = id(program)
        if iHandler.lScheduler.verifyMemorySpace(program):
            print '[interrupt] load new program: %s...' %(program.name)
            iHandler.memoryManager.load(program, idPcb)
            newPcb = PCB(idPcb, program.priority, program.sourceSize())
            self.addPCBtoReadyQueue(newPcb)
        else:
            print '[interrupt] program wait: %s...' %(program.name)
            iHandler.lScheduler.addToWaitQueue(program)


class TimeOutCommand(InterruptCommand):
    
    def iType(self):
        return InterruptHandler.TIME_OUT
    
    def executeCommand(self, iHandler):
        print '[interrupt] time out...'
        pcb = self.cpu.takePcb()
        self.addPCBtoReadyQueue(pcb)
        
        
class WaitIOCommand(InterruptCommand):
    
    def iType(self):
        return InterruptHandler.WAIT_IO
    
    def executeCommand(self, iHandler):
        print '[interrupt] wait io...'
        pcb = self.cpu.takePcb()
        iHandler.ioQueue.addPCB(pcb)
        self.addNewPCBToCPU()


class EndIOCommand(InterruptCommand):
    
    def iType(self):
        return InterruptHandler.END_IO
    
    def executeCommand(self, iHandler):
        print '[interrupt] end io...'
        pcbs = iHandler.ioQueue.removeFinishedPcbs()
        for pcb in pcbs:
            self.addPCBtoReadyQueue(pcb)


class KillCommand(InterruptCommand):
    
    def iType(self):
        return InterruptHandler.KILL
    
    def executeCommand(self, iHandler):
        print '[interrupt] finished process...'
        pcb = self.cpu.takePcb()
        iHandler.memoryManager.unload(pcb.pid)
        print '[interrupt] resources released...'
        if iHandler.lScheduler.thereProgramToLoad():
            programName = iHandler.lScheduler.getProgramToLoad()
            NewCommand(programName).execute()
