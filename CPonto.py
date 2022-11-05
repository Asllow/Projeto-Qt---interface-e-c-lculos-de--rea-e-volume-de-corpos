import numpy as np
class CPonto:
    def __init__ (self, x=0, y=0, r=0, ang=0):
        self.x = x
        self.y = y
        self.r = r
        self.ang = ang
    def conversor(self):
        self.r = (self.x**2+self.y**2)**(0.5)
        self.ang = np.degrees(np.arctan(self.y/self.x))
    def getCoordCart(self):
        return self.x, self.y
    def getCoordPol(self):
        self.conversor()
        return self.r, self.ang
    def setCoordCart(self, x=0, y=0):
        self.x = x
        self.y = y
    def setCoordPol(self, r=0, ang=0):
        self.r = r
        self.ang = ang

y = CPonto(1, 1)
r, ang = y.getCoordPol()
print(r, ang)