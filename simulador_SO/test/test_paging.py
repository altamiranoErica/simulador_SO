import unittest

from src.paging import *
from src.memory import *
from src.program import *
from src.pcb import *
from src.cpu import *
from src.disk import *

class TestScheduling(unittest.TestCase):

    def setUp(self):
        self.disk = Disk()
        self.p1 = Program("P1", ['a', 'b', 'c'])
        self.p2 = Program("P2", ['d', 'e'])
        self.p3 = Program("P3", ['f', 'g', 'h', 'i'])
        self.p4 = Program("P4", ['j', 'k', 'l', 'm'])
        
        self.disk.load("P1", self.p1)

        self.id1 = id(self.p1)
        self.pcb1 = PCB(self.id1, self.p1.priority, 3)
        self.id2 = id(self.p2)
        self.pcb2 = PCB(self.id2, self.p2.priority, 2)
        self.id3 = id(self.p3)
        self.pcb3 = PCB(self.id3, self.p3.priority, 4)
        self.id4 = id(self.p4)
        self.pcb4 = PCB(self.id4, self.p4.priority, 4)

        self.mP = Paging(Memory(), 3, self.disk)
        self.mP.load(self.p4, self.id4)
        self.mP.load(self.p3, self.id3)
        self.mP.load(self.p2, self.id2)
        self.mP.load(self.p1, self.id1)
        
    def test_read(self):
        r1 = self.mP.read(self.pcb4)
        
        self.assertEquals('j', r1)
        self.assertRaises(PageFault, self.mP.read, self.pcb1)
       
        r2 = self.mP.read(self.pcb1)
        self.assertEquals('a', r2)


if __name__ == '__main__':
    unittest.main()
