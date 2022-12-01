from multipledispatch import dispatch
class CPonto:
    @dispatch(float, float)
    def __init__ (self, x, y):
        self.x = x
        self.y = y
    @dispatch(float, float, float)
    def __init__ (self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def getCoordinatesV(self):
        return self.x, self.y, self.z
    def getCoordinatesA(self):
        return self.x, self.y
    def setCoordinatesV(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    def setCoordinatesA(self, x=0, y=0):
        self.x = x
        self.y = y
    def onlyPoint(*args):
        return list(args)