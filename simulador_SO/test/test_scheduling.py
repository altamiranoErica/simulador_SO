import unittest
from src.scheduling import *

class TestScheduling(unittest.TestCase):

    def setUp(self):
        self.fifo = ReadyQueue()
        self.priority = Priority(5)
        self.pcb1 = PCB(123, 1, 3)
        self.pcb2 = PCB(234, 1, 5)
        self.pcb3 = PCB(345, 3, 4)
        self.pcb4 = PCB(567, 4, 1)

    def test_fifo_nextPcb(self):
        self.fifo.addPCB(self.pcb1)
        self.fifo.addPCB(self.pcb2)
        
        nextPcb = self.fifo.nextPCB()

        self.assertEqual(self.pcb1, nextPcb)
        self.assertTrue(len(self.fifo.queue) == 1)

    def test_priority_nextPcb(self):
        self.priority.addPCB(self.pcb1)
        self.priority.addPCB(self.pcb2)
        self.priority.addPCB(self.pcb3)
        self.priority.addPCB(self.pcb4)
        
        nextPcb = self.priority.nextPCB()
        
        self.assertEqual(self.pcb4, nextPcb)

    def test_priority_agePCBs(self):
        self.priority.addPCB(self.pcb1)
        self.priority.addPCB(self.pcb2)
        self.priority.addPCB(self.pcb3)
        self.priority.addPCB(self.pcb4)
        
        self.priority.agePCBs()
        
        self.assertTrue(len(self.priority.matrix[-5]) == 1)
        self.assertTrue(len(self.priority.matrix[-4]) == 1)
        self.assertTrue(len(self.priority.matrix[-3]) == 0)
        self.assertTrue(len(self.priority.matrix[-2]) == 2)
        self.assertTrue(len(self.priority.matrix[-1]) == 0)

if __name__ == '__main__':
    unittest.main()
