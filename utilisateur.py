# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 15:51:05 2020

@author: rouss
"""

import math as math
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from sphere import spheres
from vect3D import Vecteur3D


"""Cette classe contient le nom,
 les coordonnées ainsi que le vecteur représentant la vision de l'utilisateur,
 et éventuellement la position de sa main."""
   
class utilisateur(object):
    
    def __init__(self,x=0,y=0,z=0,vect_vue=Vecteur3D(), main=Vecteur3D(), nom="utilisateur"):
        #Coordonnées
        self.x=x
        self.y=y
        self.z=z
        self.position=Vecteur3D(self.x,self.y,self.z)
        self.main=main #Position de la main
        #Vue de l'utilisateur
        self.vect_vue= vect_vue
        #Nom
        self.nom= nom
        
    #getters  
    def getx(self):
        return self.x
    def gety(self):
        return self.y
    def getz(self):
        return self.z
    def set_vect_vue(self,newx,newy,newz):
        self.vect_vue = Vecteur3D(newx, newy, newz)
        
    def set_position (self, newx, newy, newz):
        self.position = Vecteur3D(newx, newy, newz)
        
    def __str__(self):
        return("Utilisateur ("+self.nom+"," \
		+str(self.vect_vue)+ "," \
		+str(self.main)+ ")")
        
    def __repr__(self):
        return("Utilisateur ("+self.nom+"," \
		+str(self.vect_vue)+ "," \
		+str(self.main)+ ")")