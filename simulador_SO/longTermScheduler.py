class LongTermScheduler:
    
    def __init__(self, mManager):
        self.memoryManager = mManager
        self.waitQueue = {}
        
    def verifyMemorySpace(self, program):
        return self.memoryManager.verifyMemorySpace(program.sourceSize())
        
    def addToWaitQueue(self, program):
        self.waitQueue[program.name] = program.sourceSize()
        
    def getProgram(self, freeMemorySize):
        if self.memoryManager.verifyMemorySpace(freeMemorySize):
            return filter(lambda t: t[1] >= freeMemorySize, self.holeList().items())[0][0]
        
