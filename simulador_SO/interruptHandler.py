from interruptionCommands import *

class InterruptHandler:
    NEW = 'NEW'
    TIME_OUT = 'TIME_OUT'
    WAIT_IO = 'WAIT_IO'
    END_IO = 'END_IO'
    KILL = 'KILL'
    
    def __init__(self, interruptCommand):
        self.configurations = {}
        self.defaultConfiguration()
        
    def addConfiguration(self, interruption, command):
        self.configuration[intp] = command
        
    def interrupt(self, interruption):
        command = self.configuration[interruption]
        # cambiar a modo Kernel
        command()
        # cambiar a modo Usuario
        
    def defaultConfiguration(self):
        self.addConfiguration(InterruptHandler.NEW, self.newInterruption)
        self.addConfiguration(InterruptHandler.TIME_OUT, self.timeOutInterruption)
        self.addConfiguration(InterruptHandler.WAIT_IO, self.waitIOInterruption)
        self.addConfiguration(InterruptHandler.END_IO, self.endIOInterruption)
        self.addConfiguration(InterruptHandler.KILL, self.killInterruption)

    def newInterruption(self):
        
    def timeOutInterruption(self):
        
    def waitIOInterruption(self):
        
    def endIOInterruption(self):
        
    def killInterruption(self):
