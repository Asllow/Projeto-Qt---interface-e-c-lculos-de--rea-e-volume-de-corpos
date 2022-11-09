import sys
from PyQt5  import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUiType
#from CTriangulo import *

Ui_MainWindow, QMainWindow = loadUiType("form.ui")

class Main (QMainWindow, Ui_MainWindow):
    def __init__ (self):
        super(Main, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Cálculo de Área")
        self.area.clicked.connect(self.on_button_clicked)
    def on_button_clicked (self):
        x1 = float(self.x1.text())
        x2 = float(self.x2.text())
        x3 = float(self.x3.text())
        x4 = float(self.x4.text())
        y1 = float(self.y1.text())
        y2 = float(self.y2.text())
        y3 = float(self.y3.text())
        y4 = float(self.y4.text())
        
        result = str(x1)
        self.result.setText(result)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())