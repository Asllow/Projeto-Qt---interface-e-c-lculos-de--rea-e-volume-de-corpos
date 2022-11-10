import sys
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot
from PyQt5  import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUiType
from CShape import *

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
        p1 = CPonto(x1, y1)
        print(self.x2.text())
        
        area = CShape.areaCircle(p1)
        if self.x2.text()!=0 and self.y2.text()!=0:
            x2 = float(self.x2.text())
            y2 = float(self.y2.text())
            p2 = CPonto(x2, y2)
            area = CShape.areaCircle(p1, p2)
        result = str(area)
        self.result.setText(result)
    def on_button_clicked_triangle (self):
        x1 = float(self.x1.text())
        x2 = float(self.x2.text())
        x3 = float(self.x3.text())
        y1 = float(self.y1.text())
        y2 = float(self.y2.text())
        y3 = float(self.y3.text())
        
        p1 = CPonto(x1, y1)
        p2 = CPonto(x2, y2)
        p3 = CPonto(x3, y3)
        area = CShape.areaTriangle(p1, p2, p3)
        
        result = str(area)
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
        
        p1 = CPonto(x1, y1)
        p2 = CPonto(x2, y2)
        p3 = CPonto(x3, y3)
        p4 = CPonto(x4, y4)
        area = CShape.areaPolygon(p1, p2, p3, p4)
        
        result = str(area)
        self.result.setText(result)