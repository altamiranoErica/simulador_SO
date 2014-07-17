from interruptHandler import *

class IOQueue:

    def __init__(self, clock, timeOut=5):
        clock.addObserver(self)
        self.waitQueue = {}
        self.timeOut = timeOut
    
    def notify(self):
        self.agePCBs()
        if self.timeOut in self.waitQueue.values():
            print '[ioQueue] finish io...'
            instance_InterruptHandler().interrupt(InterruptHandler.END_IO)
        
    def addPCB(self, pcb):
        print '[ioQueue] add pcb: %s...' %(pcb.pid)
        self.waitQueue[pcb] = 0
        
    def agePCBs(self):
        for i in self.waitQueue:
            self.waitQueue[i] += 1 
    
    def removeFinishedPcbs(self):
        print '[ioQueue] remove finished pcb/s...'
        pcbList = self.waitQueue.items()
        return map(lambda t: t[0], filter(lambda t: t[1] == self.timeOut, pcbList))
        
