# modulo allocationStrategy:
#   implementa los tres algoritmos de asignacion de memoria.

class AllocationStrategy:
    def assignHole(self, program, mManager):
        raise NotImplementedError
        
    def listOfMajorHolesTo(self, size, holeList):
        return filter(lambda x: x[1] > size, holeList)

class FirstFit:
    def assignHole(self, program, mManager):
        return listOfMajorHolesTo(program.sourceSize(), mManager.holeList())[0][0]


class BestFit:
    def assignHole(self, program, mManager):
        holes = listOfMajorHolesTo(program.sourceSize(), mManager.holeList())[0][0]
        return sorted(holes, key=lambda i: i[1])[0][0]


class WorstFit:
    def assignHole(self, program, mManager):
        holes = sorted(mManager.holeList(), key=lambda i: i[1])
        holes.reverse()
        return holes[0][0]
        
