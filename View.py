import sys
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap
from PyQt5  import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUiType
import numpy as np

Ui_MainWindow, QMainWindow = loadUiType("formulario.ui")

class View (QMainWindow, Ui_MainWindow):
    def __init__ (self, model, ponto):
        super(View, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Cálculo de Área e Volume")
        self.listapontos = []
        self.model = model
        self.ponto = ponto
        self.area_curl.clicked.connect(self.on_button_clicked_circle)
        self.area.clicked.connect(self.on_button_clicked_area)
        self.volume.clicked.connect(self.on_button_clicked_volume)
        self.volume_curl.clicked.connect(self.on_button_clicked_volume_curl)
        self.adicionar.clicked.connect(self.on_add_point)
        self.limpar.clicked.connect(self.on_limpar)
    def on_limpar (self):
        self.quadro.clear()
        self.listapontos.clear()
    def on_button_clicked_circle (self):
        lista = []
        for i in self.listapontos:
            i = self.ponto(i[0], i[1])
            lista.append(i)
        print (lista)
        area = self.model.areaCircle(lista[0])
        if len(lista)>1:
            area = self.model.areaCircle(lista[0], lista[1])
        result = str(area)
        self.result.setText(result)
        self.pixmap = QPixmap('teste.png')
        self.image.setPixmap(self.pixmap)
    def on_add_point (self):
        x = float(self.x.text())
        y = float(self.y.text())
        z = float(self.z.text())
        self.quadro.appendPlainText(f"[{x}, {y}, {z}]")
        self.listapontos.append([x, y, z])
        self.x.setText("")
        self.y.setText("")
        self.z.setText("")
    def on_button_clicked_area (self):
        lista = []
        for i in self.listapontos:
            a = self.ponto(i[0], i[1])
            i = a.getCoordinatesA()
            lista.append(i)
        points = np.array(lista)
        area = self.model.area(points)
        result = str(area)
        self.result.setText(result)
        self.pixmap = QPixmap('teste.png')
        self.image.setPixmap(self.pixmap)
    def on_button_clicked_volume (self):
        lista = []
        for i in self.listapontos:
            a = self.ponto(i[0], i[1], i[2])
            i = a.getCoordinatesV()
            lista.append(i)
        points = np.array(lista)
        area = self.model.volume(points)
        result = str(area)
        self.result.setText(result)
        self.pixmap = QPixmap('teste.png')
        self.image.setPixmap(self.pixmap)
    def on_button_clicked_volume_curl (self):
        lista = []
        for i in self.listapontos:
            i = self.ponto(i[0], i[1], i[2])
            lista.append(i)
        if len(lista)<=2:
            volume = self.model.volumeEsfera(lista)
            result = str(volume)
            self.result.setText(result)
        else:
            volume = self.model.volumeC(lista)
            result = str(volume)
            self.result.setText(result)
        self.pixmap = QPixmap('teste.png')
        self.image.setPixmap(self.pixmap)