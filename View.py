import sys
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap
from PyQt5  import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUiType
from CShape import *
from scipy.spatial import ConvexHull
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from PIL import Image

Ui_MainWindow, QMainWindow = loadUiType("formulario.ui")

class View (QMainWindow, Ui_MainWindow):
    def __init__ (self):
        super(View, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Cálculo de Área e Volume")
        self.listapontos = []
        #self.area.clicked.connect(self.on_button_clicked_circle)
        self.area.clicked.connect(self.on_button_clicked_area)
        self.adicionar.clicked.connect(self.on_add_point)
        self.limpar.clicked.connect(self.on_limpar)
    def on_limpar (self):
        self.quadro.clear()
        self.listapontos.clear()
        print (self.listapontos)
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
    def on_add_point (self):
        x = float(self.x.text())
        y = float(self.y.text())
        z = float(self.z.text())
        self.quadro.appendPlainText(f"[{x}, {y}, {z}]")
        self.listapontos.append([x, y, z])
    def on_button_clicked_area (self):
        self.pixmap = QPixmap('teste.png')
        self.image.setPixmap(self.pixmap)
if __name__ == '__main__':
    rng = np.random.default_rng()
    point = np.array([[0,0,0],[10, 0, 0],[10, 10, 0],[0, 10, 0],[0, 0, 2],[10, 0, 2],[10, 10, 2],[0, 10, 2]])
    point = np.array([[0, 0],[10, 0],[10, 10],[0, 10]])
    points = np.array([[0,0,0],[3,0,0],[0,3,0],[3,3,0],[1.5,1.5,6]])
    hull = ConvexHull(points)
    print(hull.volume)
    #2D
    plt.plot(points[:,0], points[:,1], 'o')
    for simplex in hull.simplices:
        plt.plot(points[simplex, 0], points[simplex, 1], 'k-')
        
    plt.plot(points[hull.vertices,0], points[hull.vertices,1], 'r--', lw=2)
    plt.plot(points[hull.vertices[0],0], points[hull.vertices[0],1], 'ro')
    plt.savefig('teste.png', format='png')
    image = Image.open('teste.png')
    new_image = image.resize((241, 221))
    new_image.save('teste.png')
    plt.show()
    #3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.plot(points.T[0], points.T[1], points.T[2], "ko")
    
    for s in hull.simplices:
        s = np.append(s, s[0])  # Here we cycle back to the first coordinate
        ax.plot(points[s, 0], points[s, 1], points[s, 2], "r-")
    for i in ["x", "y", "z"]:
        eval("ax.set_{:s}label('{:s}')".format(i, i))
    plt.savefig('teste.png', format='png')
    image = Image.open('teste.png')
    new_image = image.resize((241, 221))
    new_image.save('teste.png')
    plt.show()