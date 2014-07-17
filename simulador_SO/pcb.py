class  PCB:

    def __init__(self, pid, priority, pSize):
        self.pid = pid
        self.priority = priority
        self.programSize = pSize
        self.pc = 0

    def incrementPc(self):
        self.pc += 1
