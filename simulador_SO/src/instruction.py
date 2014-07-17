class Instruction:
    CPU = 'CPU'
    IO = 'IO'
    
class CPUInstruction:
    
    def __init__(self, command):
        self.iType = Instruction.CPU
        self.command = command    

class CPUInstructionPrintString:
    
    def __init__(self, string):
        self.iType = Instruction.CPU
        self.command = self.iCommand(string)
    
    def iCommand(self, string):
        return lambda: '[instruction] execute print: %s' %(string)
        
class CPUInstructionPrintAdd:
    
    def __init__(self, i1, i2):
        self.iType = Instruction.CPU
        self.command = self.iCommand(i1, i2)
    
    def iCommand(self, i1, i2):
        return lambda: '[instruction] execute add: %s + %s = %s' %(i1, i2, i1 + i2)
        
class IOInstruction:
            
    def __init__(self):
        self.iType = Instruction.IO
