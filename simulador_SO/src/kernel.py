from threading import *
from interruptHandler import *
from longTermScheduler import *
from cpu import *
from clock import *
from disk import *
from ioQueue import *


class Kernel(Thread):
    
    def __init__(self, mManager, sScheduler):
        Thread.__init__(self)
        self.lock = Lock()
        self.clock = Clock(self.lock)
        self.disk = Disk()
        self.memoryManager = mManager
        self.cpu = CPU(self.memoryManager, self.clock)
        self.longScheduler = LongTermScheduler(self.memoryManager)
        self.shortScheduler = sScheduler
        self.ioQueue = IOQueue(self.clock)
        create_InterruptHandler(self.cpu, sScheduler, mManager, self.disk, self.ioQueue, self.longScheduler)
        
    def run(self):
        print('[kernel] starting...')
        self.clock.start()
        print('[kernel] started.')
    
    def startUp(self):
        self.start()

    def loadProgramToDisk(self, program):
        self.lock.acquire()
        self.disk.load(program.name, program)
        self.lock.release()
        
    def runProgram(self, nameProgram):
        self.lock.acquire()
        print('[kernel] execute new program...')
        instance_InterruptHandler().addNewProgramToLoad(nameProgram)
        instance_InterruptHandler().interrupt(InterruptHandler.NEW)
        self.lock.release()
