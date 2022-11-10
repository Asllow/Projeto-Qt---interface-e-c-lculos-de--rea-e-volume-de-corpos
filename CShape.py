from CPonto import *
from multipledispatch import dispatch
import numpy as np
import math

class CShape:
    def __init__(self, name="Generic Shape", listPoints=0, radio=0):
        self.name = name
        self.listPoints = listPoints
        self.radio = radio
    def printNome(self):
        print(self.name)
    @dispatch(float)
    def areaCircle(radio):
        return math.pi*radio**2
    @dispatch(int)
    def areaCircle(radio):
        return math.pi*radio**2
    @dispatch(CPonto)
    def areaCircle(p1):
        x1, y1 = p1.getCoordinates()
        r = (x1**2+y1**2)**(0.5)
        a = math.pi*r**2
        return a
    @dispatch(CPonto, int)
    def areaCircle(p1, radio):
        x1, y1 = p1.getCoordinates()
        a = math.pi*radio**2
        texto = f'Centro: {x1}, {y1} Área: {a}'
        return texto
    @dispatch(CPonto, CPonto)
    def areaCircle(p1, p2):
        x1, y1 = p1.getCoordinates()
        x2, y2 = p2.getCoordinates()
        r = ((x1-x2)**2+(y1-y2)**2)**(0.5)
        a = math.pi*r**2
        return a
    @dispatch (int, int)
    def areaTriangle (h , b):
        return ( b*h/2)
    @dispatch ( CPonto, CPonto, CPonto)
    def areaTriangle ( p1, p2, p3) :  
        M = np.ones((3, 3), dtype= float) 
        x1 , y1 = p1.getCoordinates()
        x2 , y2 = p2.getCoordinates() 
        x3 , y3 = p3.getCoordinates() 
        M[0, 0] = x1 
        M[0 , 1] = y1 
        M[1 , 0] = x2 
        M[1 , 1] = y2 
        M[2 , 0] = x3 
        M[2 , 1] = y3
        D=np.linalg.det(M)
        return (D/2)
    @dispatch(list)
    def areaPolygon(listPoints):
        p1 = listPoints[0]
        p2 = listPoints[1]
        p3 = listPoints[2]
        p4 = listPoints[3]
        x1, y1 = p1.getCoordinates()
        x2, y2 = p2.getCoordinates()
        x3, y3 = p3.getCoordinates()
        x4, y4 = p4.getCoordinates()
        s1 = x1*y2 + x2*y3 + x3*y4 + x4*y1
        s2 = y1*x2 + y2*x3 + y3*x4 + y4*x1
        a = (((s1 - s2)**2)**(0.5))/2
        return a
    @dispatch(CPonto, CPonto, CPonto, CPonto)
    def areaPolygon(p1, p2, p3, p4):
        x1, y1 = p1.getCoordinates()
        x2, y2 = p2.getCoordinates()
        x3, y3 = p3.getCoordinates()
        x4, y4 = p4.getCoordinates()
        s1 = x1*y2 + x2*y3 + x3*y4 + x4*y1
        s2 = y1*x2 + y2*x3 + y3*x4 + y4*x1
        a = (((s1 - s2)**2)**(0.5))/2
        return a
#atualizado