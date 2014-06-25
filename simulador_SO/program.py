class Program:
    
    def __init__(self, name, priority, instructionList):
        self.name = name
        self.priority = priority
        self.source = instructionList
        
    def sourceSize(self):
        return len(self.source)

