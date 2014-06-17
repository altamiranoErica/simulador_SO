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
        if ! self.rQueue.isEmpty()
            self.cpu.add(iHandler.queue.nextPCB())

    
class NewCommand(InterruptCommand):
    
    def executeCommand(self, iHandler):
        program = iHandler.disk.read('''nombre del programa nuevo''')
        mAddress = iHandler.memory.load(program)
        newPcb = PCB(id(program), mAddress, program.priority)
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
        pcb = iHandler.ioQueue.removeFinishedPcb()
        self.addPCBtoReadyQueue(pcb)


class KillCommand(InterruptCommand):
    
    def executeCommand(self, iHandler):
        pcb = self.cpu.takePcb()
        iHandler.memory.unload(pcb.memoryAddress)
        self.addNewPCBToCPU()
        
