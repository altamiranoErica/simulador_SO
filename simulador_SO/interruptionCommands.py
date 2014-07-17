# modulo interruptionCommands:
#   implementa las rutinas que corresponden a cada tipo de interrupcion.

class InterruptCommand:
    
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
    
    def __init__(self, pName):
        self.programName = pName
    
    def executeCommand(self, iHandler):
        program = iHandler.disk.read(self.programName)
        idPcb = id(program)
        iHandler.memoryManager.load(program, idPcb)
        newPcb = PCB(idPcb, program.priority, program.sourceSize())
        self.addPCBtoReadyQueue(newPcb)


class TimeOutCommand(InterruptCommand):
    
    def executeCommand(self, iHandler):
        pcb = self.cpu.takePcb()
        self.addPCBtoReadyQueue(pcb)
        
        
class WaitIOCommand(InterruptCommand):
    
    def executeCommand(self, iHandler):
        pcb = self.cpu.takePcb()
        iHandler.ioQueue.addPCB(pcb)
        self.addNewPCBToCPU()


class EndIOCommand(InterruptCommand):
    
    def executeCommand(self, iHandler):
        pcbs = iHandler.ioQueue.removeFinishedPcbs()
        for pcb in pcbs:
            self.addPCBtoReadyQueue(pcb)


class KillCommand(InterruptCommand):
    
    def executeCommand(self, iHandler):
        pcb = self.cpu.takePcb()
        iHandler.memoryManager.unload(pcb.pid)
        self.addNewPCBToCPU()
