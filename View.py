import sys
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot
from PyQt5  import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUiType

Ui_MainWindow, QMainWindow = loadUiType("form.ui")

class View (QMainWindow, Ui_MainWindow):
    def __init__ (self):
        super(View, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Cálculo de Área")
        
        self.area_circle.clicked.connect(self.on_button_clicked_circle)
        self.area_triangle.clicked.connect(self.on_button_clicked_triangle)
        self.area_polygon.clicked.connect(self.on_button_clicked_polygon)
    def on_button_clicked_circle (self):
        x1 = float(self.x1.text())
        y1 = float(self.y1.text())
        if self.x2.text()==True:
            x2 = float(self.x2.text())
            y2 = float(self.y2.text())
        
        result = str(x1)
        self.result.setText(result)
    def on_button_clicked_triangle (self):
        x1 = float(self.x1.text())
        x2 = float(self.x2.text())
        x3 = float(self.x3.text())
        y1 = float(self.y1.text())
        y2 = float(self.y2.text())
        y3 = float(self.y3.text())
        
        result = str(x1)
        self.result.setText(result)
    def on_button_clicked_polygon (self):
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
    view = View()
    view.show()
    sys.exit(app.exec_())