class CPonto:
    def __init__ (self, x=0, y=0, r=0, ang=0):
        self.x = x
        self.y = y
        self.r = r
        self.ang = ang
    def getCoordCard(self):
        return self.x, self.y
    def setPonto(self, x=0, y=0):
        self.x = x
        self.y = y