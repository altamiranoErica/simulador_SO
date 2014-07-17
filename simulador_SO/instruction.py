class Instruction:
    CPU = 'CPU'
    IO = 'IO'
    
class CPUInstruction:
    
    def __init__(self, command):
        self.iType = Instruction.EXECUTABLE
        self.command = command
        
class IOInstruction:
            
    def __init__(self, resourceName):
        self.iType = Instruction.IO
        self.resource = resourceName
