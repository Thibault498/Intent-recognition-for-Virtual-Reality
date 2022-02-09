# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 15:51:04 2020

@author: rouss
"""

import math as math
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


"""Nous utilisons la classe Vecteur3D pour faciliter les calculs vectoriels """

class Vecteur3D(object):
    def __init__(self, x = 0, y = 0, z = 0):
        """Constructeur avec des valeur par défaut nulles"""
        self.x = x
        self.y = y
        self.z = z
        
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_z(self):
        return self.z
        
        
    def __str__(self):
        return "Vecteur3D(%g , %g, %g)" % (self.x, self.y, self.z)
        
    def __repr__(self):
        return "Vecteur3D(%g , %g, %g)" % (self.x, self.y, self.z)
        
    def __add__(self, autre): # addition vectorielle
        if type(autre) is Vecteur3D:
            return Vecteur3D(self.x + autre.x, self.y + autre.y, self.z + autre.z)
        if type(autre) is Vecteur3DS:
            tmp = autre.carthesien()
            return Vecteur3D(self.x + tmp.x, self.y + tmp.y, self.z + tmp.z)
    
    def __neg__(self):
        return Vecteur3D(-self.x,-self.y, -self.z)
        
    def __sub__(self,autre):
        return self + (-autre)
    
    def __mul__(self,autre):
        """vectoriel entre 2 vecteur3D, sinon scalaire"""
        if type(autre) is Vecteur3D :
            X = self.y*autre.z - self.z*autre.y
            Y = self.z*autre.x - self.x*autre.z
            Z = self.x*autre.y - self.y*autre.x
            
            return Vecteur3D(X,Y,Z)
            
        
        
        else:
            return Vecteur3D(autre*self.x,autre*self.y,autre*self.z)
    
    def __rmul__(self,autre):
        return self * autre
        
    def __pow__(self,autre):
        """scalaire entre deux Vecteurs3D, puissance entre Vecteur3D et scalaire"""
        if type(autre) is Vecteur3D :
            return self.x * autre.x +self.y * autre.y +self.z * autre.z
        
        else :
            v = self
            for i in range(1,int(autre)):
                if type(v) is Vecteur3D:
                    v = self ** v
                else :
                    v = self * v
            return v
      
    def __truediv__(self,autre):
        return 1/autre * self
        
    def mod(self):
        """La norme du Vecteur3D"""
        n=(self.x * self.x + self.y * self.y + self.z * self.z)**.5
        return n
        
    def norm(self):
        """Vecteur Normalisé"""
        return self/self.mod()
        
    def normalise(self):
        """normalisé le vecteur"""
        tmp = self/self.mod()
        self.x = tmp.x
        self.y = tmp.y
        self.z = tmp.z
        
        