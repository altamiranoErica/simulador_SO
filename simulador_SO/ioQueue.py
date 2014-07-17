from interruptHandler import *

class IOQueue:

    def __init__(self, clock, timeOut):
        clock.addObserver(self)
        self.waitQueue = {}
        self.timeOut = timeOut
    
    def notify(self):
        self.agePCBs()
        if 0 in self.waitQueue.values():
            instance_InterruptHandler().interrupt(InterruptHandler.END_IO)
        
    def addPCB(self, pcb):
        self.waitQueue[pcb] = 0
        
    def agePCBs(self):
        for i in self.waitQueue:
            self.waitQueue[i] += 1 
    
    def removeFinishedPcbs(self):
        pcbList = self.waitQueue.items()
        return map(lambda t: t[0], filter(lambda t: t[1] == 0, pcbList))
        
