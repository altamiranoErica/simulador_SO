from interruptionCommands import *

class InterruptHandler():
    NEW = 'NEW'
    TIME_OUT = 'TIME_OUT'
    WAIT_IO = 'WAIT_IO'
    END_IO = 'END_IO'
    KILL = 'KILL'
    
    _instance = None
    
    def __init__(self, cpu, rQueue, mManager, disk, ioQueue):
        self.cpu = cpu
        self.readyQueue = rQueue
        self.memoryManager = mManager
        self.disk = disk
        self.ioQueue = ioQueue
        self.configuration = {}
        self.defaultConfiguration()

    def addConfiguration(self, interruption, command):
        self.configuration[interruption] = command
        
    def interrupt(self, interruption):
        command = self.configuration[interruption]
        command.execute(self)
        
    def defaultConfiguration(self):
        self.addConfiguration(InterruptHandler.NEW, NewCommand())
        self.addConfiguration(InterruptHandler.TIME_OUT, TimeOutCommand())
        self.addConfiguration(InterruptHandler.WAIT_IO, WaitIOCommand())
        self.addConfiguration(InterruptHandler.END_IO, EndIOCommand())
        self.addConfiguration(InterruptHandler.KILL, KillCommand())

def create_InterruptHandler(cpu, rQueue, mManager, disk, ioQueue):
    # Crea la instancia de InterruptHandler si esta aun no fue creada.
    if not InterruptHandler._instance:
        InterruptHandler._instance = InterruptHandler(cpu, rQueue, mManager, disk, ioQueue)

def instance_InterruptHandler():
    '''Retorna la instancia unica de InterruptHandler.
       Condicion: Haber creado primero la instancia.'''
    if not InterruptHandler._instance:
        raise RuntimeError, 'Es necesario crear el Handler de interrupcion para poder utilizarlo'
    return InterruptHandler._instance
