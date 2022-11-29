class CPonto:
    def __init__ (self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    def getCoordinates(self):
        return self.x, self.y, self.z
    def setCoordinates(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    def onlyPoint(*args):
        return list(args)