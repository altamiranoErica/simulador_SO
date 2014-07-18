import unittest
from mockito import *
from src.allocationStrategy import *

class TestAllocationStrategy(unittest.TestCase):

    def setUp(self):
        self.ff = FirstFit()
        self.bf = BestFit()
        self.wf = WorstFit()
        self.mm = mock()
        when(self.mm).holeList().thenReturn({8: 2, 3: 3, 10: 5})

    def test_ff_assignHole(self):
        addressHole = self.ff.assignHole(2, self.mm)

        self.assertEqual(3, addressHole)

    def test_bf_assignHole(self):
        addressHole = self.bf.assignHole(2, self.mm)

        self.assertEqual(8, addressHole)

    def test_wf_assignHole(self):
        addressHole = self.wf.assignHole(2, self.mm)

        self.assertEqual(10, addressHole)
    
if __name__ == '__main__':
    unittest.main()
