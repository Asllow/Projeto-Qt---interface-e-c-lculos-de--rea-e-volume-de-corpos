import numpy as np

class CPonto:
    def __init__ (self, x=0, y=0, r=0, ang=0):
        self.x = x
        self.y = y
        self.r = r
        self.ang = np.radians(ang)
    def conversorCart(self):
        self.x = self.r*np.cos(self.ang)
        self.y = self.r*np.sin(self.ang)
    def conversorPol(self):
        self.r = (self.x**2+self.y**2)**(0.5)
        self.ang = np.degrees(np.arctan(self.y/self.x))
    def getCoordCart(self):
        if (self.ang==0 and self.r==0):
            return self.x, self.y
        else:
            self.conversorCart()
            return self.x, self.y
    def getCoordPol(self):
        if (self.x==0 and self.y==0):
            return self.r, self.ang
        else:
            self.conversorPol()
            return self.r, self.ang
    def setCoordCart(self, x=0, y=0):
        self.x = x
        self.y = y
    def setCoordPol(self, r=0, ang=0):
        self.r = r
        self.ang = ang