# modulo allocationStrategy:
#   implementa los tres algoritmos de asignacion de memoria.

class AllocationStrategy:
    def assignHole(self, programSize, mManager):
        raise NotImplementedError
        
    def listOfMajorHolesTo(self, size, holeList):
        orderedHoles = holeList.items()
        orderedHoles.sort(key=lambda i: i[0])
        return filter(lambda x: x[1] > size, orderedHoles)

class FirstFit(AllocationStrategy):
    def assignHole(self, programSize, mManager):
        return self.listOfMajorHolesTo(programSize, mManager.holeList())[0][0]


class BestFit(AllocationStrategy):
    def assignHole(self, programSize, mManager):
        holes = self.listOfMajorHolesTo(programSize, mManager.holeList())
        holes.sort(key=lambda i: i[1])
        return holes[0][0]


class WorstFit(AllocationStrategy):
    def assignHole(self, programSize, mManager):
        holes = mManager.holeList().items()
        holes.sort(key=lambda i: i[1])
        return holes[len(holes)-1][0]
        
