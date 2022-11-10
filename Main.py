import sys
from PyQt5.QtWidgets import QApplication
from View import View
from CShape import CShape as Model

class App (QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        
        self.model = Model()
        self.view = View()
        self.view.show()

if __name__ == "__main__":
    app = App(sys.argv)
    sys.exit(app.exec_())