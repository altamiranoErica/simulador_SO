class LongTermScheduler:
    
    def __init__(self, mManager):
        self.memoryManager = mManager
        self.waitQueue = {}
        
    def verifyMemorySpace(self, program):
        return self.memoryManager.verifyMemorySpace(program.sourceSize())
        
    def addToWaitQueue(self, program):
        self.waitQueue[program.name] = program.sourceSize()
        
    def thereProgramToLoad(self):
        return len(self.programsToLoad()) > 0
    
    def programsToLoad(self):
        programs = filter(lambda t: self.memoryManager.verifyMemorySpace(t[1]), self.waitQueue)
        return map(lambda t: t[0], programs)
        
    def getProgramToLoad(self):
        program = self.programsToLoad()[0]
        self.waitQueue.pop(program)
        return program
