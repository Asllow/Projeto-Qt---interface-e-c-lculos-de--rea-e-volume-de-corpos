class CPonto:
    def __init__ (self, x=0, y=0):
        self.x = x
        self.y = y
    def getCoordenadas(self):
        return self.x, self.y
    def setPonto(self, x=0, y=0):
        self.x = x
        self.y = y