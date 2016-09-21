
class Point:
    '''
    Point which has 4 variables. The cordinations of x,y,z and index for algorithm.
    '''
    x = 0
    y = 0
    z = 0
    index = 0
    father = 0

    def __init__(self, x, y, z, index = 0):
        self.x = x
        self.y = y
        self.z = z
        self.index = index

    def editIndex(self, index):
        self.index = index

    def getCoordinate(self):
        return [self.x,self.y,self.z]

    def setFather(self, father):
        self.father = father

    def getFather(self):
        return self.father

    def __repr__(self):
        return str(self.x)+" "+str(self.y)+" "+str(self.z)+" "+str(self.index)
