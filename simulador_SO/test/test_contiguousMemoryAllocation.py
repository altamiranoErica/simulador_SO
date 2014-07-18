import unittest
from mockito import *

from src.memoryManager import *
from src.memory import *
from src.allocationStrategy import *

class TestContiguousMemoryAllocation(unittest.TestCase):

    def setUp(self):
        self.m = MemoryPool('pcb1', 0, 3)
        self.m2 = MemoryPool('pcb2', 10, 4)
        self.m1 = MemoryPool('pcb3', 6, 2)

        self.cMA = ContiguousMemoryAllocation(Memory(), FirstFit())
        self.cMA.allocationList = [self.m, self.m1, self.m2]

    def test_holeList(self):
        holeList = self.cMA.holeList().items()

        self.assertTrue((3,3) in holeList)
        self.assertTrue((8,2) in holeList)
        self.assertTrue((14,1) in holeList) # la memoria tiene tamanio 15 por defecto.
        
if __name__ == '__main__':
    unittest.main()
