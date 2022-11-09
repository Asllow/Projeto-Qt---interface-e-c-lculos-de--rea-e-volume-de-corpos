class CPonto:
    def __init__ (self, x=0, y=0):
        self.x = x
        self.y = y
    def getCoordenates(self):
        return self.x, self.y
    def setCoordenates(self, x=0, y=0):
        self.x = x
        self.y = y