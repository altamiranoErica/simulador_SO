class CPU:

    def __init__(self, mManager):
        self.memoryManager = mManager
        
    def addPcb(self, pcb):
        self.pcb = pcb    
    
    #def execute(self, instruction):
        
    def fetch(self):
        instruction = self.memoryManager.read(pcb)
        pcb.incrementPc()
        self.execute(instruction)
        
    def notify(self):
        self.fetch()
