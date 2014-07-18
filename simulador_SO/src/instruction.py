class Instruction:
    CPU = 'CPU'
    IO = 'IO'

class CPUInstruction:
    
    def __init__(self, iName):
        self.iType = Instruction.CPU
        self.name = iName
    
    def execute(self):
        print 'Execute instruction: %s' %(self.name)
        
class IOInstruction:
            
    def __init__(self):
        self.iType = Instruction.IO
