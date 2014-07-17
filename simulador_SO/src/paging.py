import memoryManager
from memoryFrames import *

class Paging(memoryManager.MemoryManager):
    
    def __init__(self, memory, pSize, disk):
        self.memoryF = MemoryFrames(memory, pSize)
        self.pageSize = pSize
        self.disk = disk
        self.pagesTable = []
        
    def verifyMemorySpace(self, size):
        return True
    
    def load(self, program, idPcb):
        pAmount = self.calculateNumberOfPages(program.sourceSize())
        for i in range(pAmount):
            page = Page(i + 1, self.pageSize)
            cell = PageTableCell(idPcb, program.name, page)
            if not len(self.memoryF.freeFrames()) == 0:
                frame = self.memoryF.nextFreeFrame()
                self.memoryF.loadFrame(frame, program.source, i)
                cell.addFrameNumber(frame.number)
            self.pagesTable.append(cell)
    
    def calculateNumberOfPages(self, programSize):
        if not programSize%self.pageSize == 0:
            return programSize / self.pageSize + 1
        else:
            return programSize / self.pageSize
            
    def unload(self, pcb):
        pageCells = filter(lambda pCell: pCell.idPcb == pcb.pid, self.pagesTable)
        for pCell in pageCells:
            nameOnsDisk = '%s - %s' %(pCell.idPcb, pCell.page.number)
            print nameOnsDisk
            if self.disk.containsName(nameOnsDisk):
                self.disk.delete(nameOnsDisk)
            self.memoryF.emptyFrame(pCell.frameNumber)
            self.pagesTable.remove(pCell)
        
    def read(self, pcb):
        pageCells = filter(lambda pCell: pCell.idPcb == pcb.pid, self.pagesTable)
        numberPage = pcb.pc/self.pageSize + 1
        offset = pcb.pc%self.pageSize
        pCell = [p for p in pageCells if p.page.number == numberPage][0]
        if pCell.page.isRead:
            self.memoryF.increaseDisuse(pCell.frameNumber)
            return self.memoryF.readFrame(pCell.frameNumber, offset)
        else:
            self.swap(pCell)
            raise PageFault()
            
    def swap(self, pageCell):
        fVictim = self.memoryF.leastRecentlyUsed()
        self.generateBackupAndReleaseFrame(fVictim)
        if pageCell.isOnDisk():
            self.searchOldFrameAndLoad(pageCell)
        else:
            self.loadNewFrame(pageCell)
            
    def generateBackupAndReleaseFrame(self, frame):
        backUp = BackUpFrame(frame, self.memoryF.getSourceFrame(frame))
        linkedCell = filter(lambda pCell: pCell.frameNumber == frame.number, self.pagesTable)[0]
        idBackUp = '%s - %s' %(linkedCell.idPcb, linkedCell.page.number)
        self.disk.load(idBackUp, backUp)
        linkedCell.page.changeRead()
        
    def searchOldFrameAndLoad(self, pageCell):
        oldBackUp = self.disk.read('%s - %s' %(pageCell.idPcb, pageCell.page.number))
        frame = self.memoryF.nextFreeFrame()
        frame.counter = oldBackUp.fCounter
        self.memoryF.loadInstructionList(frame, oldBackUp.fInstructionList)
        pageCell.addFrameNumber(frame.number)
        
    def loadNewFrame(self, pageCell):
        frame = self.memoryF.nextFreeFrame()
        program = self.disk.read(pageCell.programName)
        self.memoryF.loadFrame(frame, program.source, pageCell.page.number-1)
        pageCell.addFrameNumber(frame.number)

class PageTableCell:
    
    def __init__(self, idPcb, programName, page):
        self.idPcb = idPcb
        self.programName = programName
        self.page = page
        self.frameNumber = None
        
    def addFrameNumber(self, fNumber):
        self.frameNumber = fNumber
        self.page.changeRead()
        
    def isOnDisk(self):
        return (not self.page.isRead) and (self.frameNumber is not None)


class Page:
    
    def __init__(self, pNumber, pSize):
        self.number = pNumber
        self.size = pSize
        self.isRead = False
        
    def changeRead(self):
        self.isRead = not self.isRead
        
class BackUpFrame:
    
    def __init__(self, frame, instructionList):
        self.fCounter = frame.counter
        self.fInstructionList = instructionList
        
        
class PageFault(Exception):
    
    def __str__(self):
        return repr('Can not complete the reading, page fault.')

        
        
        
