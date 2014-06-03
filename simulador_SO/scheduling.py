# modulo Scheduling.

from collections import deque

class ReadyQueue:
    # Implementa el algoritmo FIFO por defecto.
    
    def __init__(self):
        self.queue = deque([])
    
    def addPCB(self, pcb):
        self.queue.append(pcb)
    
    def nextPCB(self):
        return self.queue.popleft()

    def removePCB(self, pcb):
        self.queue.remove(pcb)
    
	def isEmpty(self):
		return len(self.queue) == 0
        
class Priority:
    
    def __init__(self, readyQueue, topPriority):
        self.readyQueue = readyQueue
        self.queueToMatrix()
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
        self.readyQueue.addPCB(pcb)
            # informacion duplicada.
    
    def nextPCB(self):
        nextPcb = self.searchNext(self.topPriority)
        self.agePCBs()
        return nextPcb
        
    def searchNext(self, priority):
        if len(self.matrix[-priority]) == 0:
            pcb = searchNext(priority - 1)
        else:
            pcb = self.matrix[-priority].pop(0)
            self.readyQueue.removePCB(pcb)
        return pcb
    
    def agePCBs(self):
        self.matrix[-self.topPriority].extend(self.matrix[-(self.topPriority - 1)])
        self.rotateList(self.topPriority - 1)
        self.matrix[-1] = []
            # la prioridad minima es 1.
    
    def rotateList(self, maxIndex):
        # Mueve cada lista a un nivel superior en la matriz.
        for i in (r = [maxIndex - x for x in range(maxIndex - 1)]):
            self.matrix[-i] = self.matrix[-(i-1)]
    
    def isEmpty(self):
		return self.readyQueue.isEmpty()

class RoundRobin:
    ''' Para aplicar RoundRobin con prioridad solo se debe pasar por
    parametro un intancia de la clase *Priority*. Por ser polimorficas
    el algoritmo sigue funcionando correctamente'''
    
    def __init__(self, readyQueue, quantum, clock):
        self.queue = readyQueue
        self.timer = Quantum(quantum, clock)
        
    def addPCB(self, pcb):
        self.queue.addPCB(pcb)
    
    def nextPCB(self):
        return self.queue.nextPCB()
    
	def isEmpty(self):
		return self.queue.isEmpty()
    
class Quantum:
	
	def __init__(self, quantum, clock):
		self.quantum = quantum
		self.countQ = quantum
		self.clock.addObserver(self)
    
	def notify(self):
		if self.countQ > 1:
			self.countQ -= 1
		else:
			self.restart()
			# lanzar interrupcion *timeOut*
    
	def restart(self):
		self.countQ = self.quantum
