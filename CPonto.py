import numpy as np
class CPonto:
    def __init__ (self, x=0, y=0, r=0, ang=0):
        self.x = x
        self.y = y
        self.r = r
        self.ang = ang
    def getCoordCard(self):
        return self.x, self.y
    def setCoordCart(self, x=0, y=0):
        self.x = x
        self.y = y
    def conversor(self):
        self.r = (self.x**2+self.y**2)**(0.5)
        self.ang = np.arctan(self.y/self.x)