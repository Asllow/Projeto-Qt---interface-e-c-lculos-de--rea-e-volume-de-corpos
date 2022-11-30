from CPonto import *
import numpy as np
import math
from scipy.spatial import ConvexHull
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from PIL import Image

class CShape:
    def __init__(self, name="Generic Shape", listPoints=0, radio=0):
        self.name = name
        self.listPoints = listPoints
        self.radio = radio
    def printNome(self):
        print(self.name)
    @dispatch(float)
    def areaCircle(radio):
        return abs(math.pi*radio**2)
    @dispatch(int)
    def areaCircle(radio):
        return math.pi*radio**2
    @dispatch(CPonto)
    def areaCircle(p1):
        x1, y1 = p1.getCoordinatesA()
        r = (x1**2+y1**2)**(0.5)
        a = abs(math.pi*r**2)
        return a
    @dispatch(CPonto, int)
    def areaCircle(p1, radio):
        x1, y1 = p1.getCoordinates()
        a = abs(math.pi*radio**2)
        texto = f'Centro: {x1}, {y1} Área: {a}'
        return texto
    @dispatch(CPonto, CPonto)
    def areaCircle(p1, p2):
        x1, y1 = p1.getCoordinatesA()
        x2, y2 = p2.getCoordinatesA()
        r = ((x1-x2)**2+(y1-y2)**2)**(0.5)
        a = abs(math.pi*r**2)
        return a
    def area(points):
        hull = ConvexHull(points)
        plt.plot(points[:,0], points[:,1], 'o')
        for simplex in hull.simplices:
            plt.plot(points[simplex, 0], points[simplex, 1], 'k-')
        plt.plot(points[hull.vertices,0], points[hull.vertices,1], 'r--', lw=2)
        plt.plot(points[hull.vertices[0],0], points[hull.vertices[0],1], 'ro')
        plt.savefig('teste.png', format='png')
        image = Image.open('teste.png')
        new_image = image.resize((241, 221))
        new_image.save('teste.png')
        area = round(hull.volume, 2)
        return area
    def volume(points):
        hull = ConvexHull(points)
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
        area = round(hull.volume, 2)
        return area
    def volumeEsfera(lista):
        if len(lista) == 1:
            x1, y1, z1 = lista[0].getCoordinatesV()
            r = (x1**2 + y1**2)**0.5
        else:
            x1, y1, z1 = lista[0].getCoordinatesV()
            x2, y2, z2 = lista[1].getCoordinatesV()
            r = ((x1-x2)**2 + (y1-y2)**2)**0.5
        volume = round((4/3)*math.pi*r**3, 2)
        return volume
    def volumeC(lista):
        x1, y1, z1 = lista[0].getCoordinatesV()
        x2, y2, z2 = lista[1].getCoordinatesV()
        x3, y3, z3 = lista[2].getCoordinatesV()
        listX = [x2, x3]
        listY = [y2, y3]
        listZ = [z1, z2, z3]
        xm = max(listX)
        ym = max(listY)
        h = max(listZ)
        r = ((x1-xm)**2 + (y1-ym)**2)**0.5
        if (x2==x3) and (y2==y3):
            volume = round(h*math.pi*r**2,2)
        else:
            volume = round((h*math.pi*r**2)/3,2)
        return volume