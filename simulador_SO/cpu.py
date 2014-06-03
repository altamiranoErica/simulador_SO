class CPU:

    def __init__(self, memory):
        self.memory = memory
        
    def addPcb(self, pcb):
        self.pcb = pcb    
    
    def execute(self, instruction):
        
    def fetch(self):
        memoryAddress = self.pcb.memoryAddress + self.pcb.pc
        instruction = self.memory.read(memoryAddress)
        pcb.incrementPc()
        self.execute(instruction)
        
    def notify(self):
        self.fetch()
