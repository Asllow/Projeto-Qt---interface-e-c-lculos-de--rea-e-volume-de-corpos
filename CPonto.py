class CPonto:
    def __init__ (self, x=0, y=0):
        self.x = x
        self.y = y
    def getCoordinates(self):
        return self.x, self.y
    def setCoordinates(self, x=0, y=0):
        self.x = x
        self.y = y
    def onlyPoint(*args):
        return list(args)