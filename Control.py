import sys
from PyQt5.QtWidgets import QApplication
from View import View
from Model import *

class App (QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        
        self.model = CShape
        self.ponto = CPonto
        self.view = View(self.model, self.ponto)
        self.view.show()

if __name__ == "__main__":
    app = App(sys.argv)
    sys.exit(app.exec_())