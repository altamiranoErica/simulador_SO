# modulo Scheduling.
from interruptHandler import *
from collections import *

class ReadyQueue:
    # Implementa el algoritmo FIFO por defecto.
    
    def __init__(self):
        self.queue = deque([])
    
    def addPCB(self, pcb):
        print '[readyQueue] add pcb: %s...' %(pcb.pid)
        self.queue.append(pcb)
    
    def nextPCB(self):
        return self.queue.popleft()

    def removePCB(self, pcb):
        print '[readyQueue] remove pcb: %s...' %(pcb.pid)
        self.queue.remove(pcb)
	
    def isEmpty(self):
        return len(self.queue) == 0
		
        
class Priority:
    
    def __init__(self, topPriority):
        #self.readyQueue = readyQueue
        #self.queueToMatrix()
        self.matrix = [[] for i in range(topPriority)]
        self.topPriority = topPriority
        
    def queueToMatrix(self):
        self.matrix = [[] for i in range(self.topPriority)]
        for i in self.readyQueue:
            self.matrix[-i.priority].append(i)
            ''' usa indices negativos para evitar el tener que restar
            uno. En adelante SIEMPRE se usa *-i* para acceder a los
            elementos de prioridad *i*. '''
        
    def addPCB(self, pcb):
        self.matrix[-pcb.priority].append(pcb)
        #self.readyQueue.addPCB(pcb)
    
    def nextPCB(self):
        nextPcb = self.searchNext(self.topPriority)
        self.agePCBs()
        return nextPcb
        
    def searchNext(self, priority):
        if len(self.matrix[-priority]) == 0:
            pcb = self.searchNext(priority - 1)
        else:
            pcb = self.matrix[-priority].pop(0)
            #self.readyQueue.removePCB(pcb)
        return pcb
    
    def agePCBs(self):
        self.matrix[-self.topPriority].extend(self.matrix[-(self.topPriority - 1)])
        self.rotateList(self.topPriority - 1)
        self.matrix[-1] = []
            # la prioridad minima es 1.
    
    def rotateList(self, maxIndex):
        # Mueve cada lista a un nivel superior en la matriz.
        for i in ([maxIndex - x for x in range(maxIndex - 1)]):
            self.matrix[-i] = self.matrix[-(i-1)]
    
    def isEmpty(self):
        return self.readyQueue.isEmpty()

class RoundRobin:
    ''' Para aplicar RoundRobin con prioridad solo se debe pasar por
    parametro un intancia de la clase *Priority*. Por ser polimorficas
    el algoritmo sigue funcionando correctamente'''
    
    def __init__(self, readyQueue, quantum, clock, cpu):
        self.queue = readyQueue
        self.timer = Quantum(quantum, clock, cpu)
        
    def addPCB(self, pcb):
        self.queue.addPCB(pcb)
    
    def nextPCB(self):
        return self.queue.nextPCB()
    
    def isEmpty(self):
        return self.queue.isEmpty()
    
class Quantum:
	
    def __init__(self, quantum, clock, cpu):
        self.quantum = quantum
        self.counterQ = quantum
        self.cpu = cpu
        clock.removeObserver(cpu)
        clock.addObserver(self)
    
    def notify(self):
        if self.counterQ > 0:
            self.counterQ -= 1
            self.cpu.notify()
        else:
            self.restart()
            instance_InterruptHandler().interrupt(InterruptHandler.TIME_OUT)
    
    def restart(self):
        self.counterQ = self.quantum
