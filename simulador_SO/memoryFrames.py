class MemoryFrames:
    
    def __init__(self, memory, fSize):
        self.memory = memory
        self.frameSize = fSize
        self.memoryFramesAddress = self.separateMemoryFrames()
        self.framesUsed = []
        
    def separateMemoryFrames(self):
        frameAddressList = []
        count = self.memory.size/self.frameSize
        for a, n in zip([x*self.frameSize for x in range(count)], range(count)):
            frame = Frame(n, self.memory.firstCell() + a)
            frameAddressList.append(frame)
        return frameAddressList
        
    def freeFrames(self):
        freeFrames = set(self.memoryFramesAddress) - set(self.framesUsed)
        return list(freeFrames)
    
    def nextFreeFrame(self):
        nextFrame = self.freeFrames().pop()
        self.framesUsed.append(nextFrame)
        return nextFrame
        
    def loadFrame(self, frame, instructionList, pageNumber):
        startRange = pageNumber*self.frameSize
        endRange = pageNumber*self.frameSize+self.frameSize
        for i, a in zip(instructionList[startRange:endRange], range(self.frameSize)):
            self.memory.loadInstruction(frame.memoryAddress + a, i)
            
    def loadInstructionList(self, frame, instructionList):
        for i, a in zip(instructionList, range(self.frameSize)):
            self.memory.loadInstruction(frame.memoryAddress + a, i)
            
    def readFrame(self, frameNumber, offset):
        frame = filter(lambda f: f.number == frameNumber, self.framesUsed)[0]
        return self.memory.read(frame.memoryAddress + offset)
    
    def getSourceFrame(self, frame):
        iList = []
        for i in range(self.frameSize):
            iList.append(self.memory.read(frame.memoryAddress + i))
        return iList
    
    def increaseDisuse(self, currentFrame):
        for f in self.framesUsed:
            if not f.number == currentFrame:
                f.incrementCount()
    
    def leastRecentlyUsed(self):
        self.framesUsed.sort(key=lambda f: f.counter)
        victim = self.framesUsed[len(self.framesUsed)-1]
        self.framesUsed.remove(victim)
        return victim
        
    def getFrame(self, frameNumber):
        return filter(lambda f: f.number == frameNumber, self.memoryFramesAddress)[0]
    
    def emptyFrame(self, frameNumber):
        self.framesUsed.remove(self.getFrame(frameNumber))

class Frame:
    
    def __init__(self, fNumber, mAddress):
        self.number = fNumber
        self.memoryAddress = mAddress
        self.counter = 0
        #self.instructionAmount = 0
    
    def incrementCount(self):
        self.counter += 1
