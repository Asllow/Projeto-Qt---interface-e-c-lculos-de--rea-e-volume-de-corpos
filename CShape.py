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
        return abs(math.pi*radio**2)
    @dispatch(int)
    def areaCircle(radio):
        return math.pi*radio**2
    @dispatch(CPonto)
    def areaCircle(p1):
        x1, y1 = p1.getCoordinates()
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
        x1, y1 = p1.getCoordinates()
        x2, y2 = p2.getCoordinates()
        r = ((x1-x2)**2+(y1-y2)**2)**(0.5)
        a = abs(math.pi*r**2)
        return a
    dispatch(list, list)
    def area(x,y):
        return 0.5*np.abs(np.dot(x,np.roll(y,1))-np.dot(y,np.roll(x,1)))
    @dispatch (int, int)
    def areaTriangle (h , b):
        return abs( b*h/2)
    @dispatch (CPonto, CPonto, CPonto)
    def areaTriangle (p1, p2, p3) :  
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
        D=abs(np.linalg.det(M))
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
        listpoints = [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]
        listpoints.sort()
        
        M = np.ones((3, 3), dtype= float)
        N = np.ones((3, 3), dtype= float) 
        
        M[0, 0] = listpoints[0][0]
        M[0 , 1] = listpoints[0][1]
        M[1 , 0] = listpoints[1][0]
        M[1 , 1] = listpoints[1][1]
        M[2 , 0] = listpoints[2][0]
        M[2 , 1] = listpoints[2][1]
        D= (abs(np.linalg.det(M)))/2
        
        N[0, 0] = listpoints[3][0]
        N[0 , 1] = listpoints[3][1]
        N[1 , 0] = listpoints[1][0]
        N[1 , 1] = listpoints[1][1]
        N[2 , 0] = listpoints[2][0]
        N[2 , 1] = listpoints[2][1]
        P= (abs(np.linalg.det(N)))/2
        
        area = abs(D+P)
        return area
    @dispatch(CPonto, CPonto, CPonto, CPonto)
    def areaPolygon(p1, p2, p3, p4):
        x1, y1 = p1.getCoordinates()
        x2, y2 = p2.getCoordinates()
        x3, y3 = p3.getCoordinates()
        x4, y4 = p4.getCoordinates()
        listpoints = [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]
        listpoints.sort()
        
        M = np.ones((3, 3), dtype= float)
        N = np.ones((3, 3), dtype= float) 
        
        M[0, 0] = listpoints[0][0]
        M[0 , 1] = listpoints[0][1]
        M[1 , 0] = listpoints[1][0]
        M[1 , 1] = listpoints[1][1]
        M[2 , 0] = listpoints[2][0]
        M[2 , 1] = listpoints[2][1]
        D= (abs(np.linalg.det(M)))/2
        
        N[0, 0] = listpoints[3][0]
        N[0 , 1] = listpoints[3][1]
        N[1 , 0] = listpoints[1][0]
        N[1 , 1] = listpoints[1][1]
        N[2 , 0] = listpoints[2][0]
        N[2 , 1] = listpoints[2][1]
        P= (abs(np.linalg.det(N)))/2
        
        area = abs(D+P)
        return area