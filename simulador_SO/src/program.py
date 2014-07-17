class Program:
    
    def __init__(self, name, instructionList, pPriority = 1):
        self.name = name
        self.priority = pPriority
        self.source = instructionList
        
    def sourceSize(self):
        return len(self.source)

