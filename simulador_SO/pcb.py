class  PCB:

    def __init__(self, pid, mAddress, priority):
        self.pid = pid
        self.memoryAddress = mAddress
        self.priority = priority
        self.pc = 0

    def incrementPc(self):
        self.pc = self.pc + 1
