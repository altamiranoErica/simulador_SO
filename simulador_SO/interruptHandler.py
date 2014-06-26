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
        command.execute(this)
        
    def defaultConfiguration(self):
        self.addConfiguration(InterruptHandler.NEW, NewCommand())
        self.addConfiguration(InterruptHandler.TIME_OUT, TimeOutCommand())
        self.addConfiguration(InterruptHandler.WAIT_IO, WaitIOCommand())
        self.addConfiguration(InterruptHandler.END_IO, EndIOCommand())
        self.addConfiguration(InterruptHandler.KILL, KillCommand())
