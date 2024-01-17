from math import pi 
from math import sqrt
from math import atan2


class Point:
    def __init__(self,abs:float,ord:float):
        self._abs = abs
        self._ord = ord
        self._r = sqrt(self._abs**2 + self._ord**2)
        self._a = atan2(self._ord,self._abs)*360/(2*pi)

    def get_abs(self):
        return self._abs
    
    def get_ord(self):
        return self._ord
    
    def set_abs(self,abs):
        self._abs = abs

    def set_ord(self,ord):
        self._ord = ord
    
    def get_r(self):
        return self._r
    
    def set_r(self, r):
        self._r = r
    
    def get_a(self):
        return self._a
    
    def set_a(self,a):
        self._a = a

    def deplace(self,dx:float,dy:float):
        self._abs += dx
        self._ord += dy

    def sym_x(self):
        self._ord = -(self._ord)

    def sym_y(self):
        self._abs = -(self._abs)

    #def sym_0(self):
    #    self._ord = -self._ord
    #    self._abs = -self._abs

if __name__ == "__main__":
    #p = Point(0.0, 0.0)
    #print(p._abs,p._ord)
    #print(p.get_abs(),p.get_ord())#accesseur en lecture
    #p.set_abs(1.0),p.set_ord(1.0)#mutateur
    #print(p.get_abs(),p.get_ord())#accesseur en lecture
    #p.set_r(3)#mutateur
    #print(p.get_r())
    #p1 = p.deplace(1.0,1.0)
    p1= Point(1.0,2.0)
    print(p1.get_abs(),p1.get_ord())
    p1.sym_y()
    print("Symetrie par rapport a y :",p1.get_abs(), p1.get_ord()) #-1.0,2.0
    p1.sym_x()
    print("Symetrie par rapport a x et y :",p1.get_abs(),p1.get_ord())#-1.0,-2.0
    p1.sym_y()
    print("Symetrie par rapport a x :",p1.get_abs(),p1.get_ord())#1.0,-2.0
    p2 = Point(1.0,1.0)
    #p2.sym_0()
    print(p2.get_abs(),p2.get_ord())
    
