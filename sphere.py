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
from vect3D import Vecteur3D


"""La classe spheres contient les coordonnées de chaque objet,
ainsi que les différents scores évaluant la probabilité d'intéraction de l'utilisateur avec l'objet,
en fonction du critère d'évaluation."""
class spheres(object):
    def __init__(self,x,y,z, prob_angle=0, prob_dist=0, prob_tot=0,dist=[],prob_main=0,nom="sphère",couleur='red',taille=0, activation = 0, reconnu=0):
        #coordonnées
        self.x=x
        self.y=y
        self.z=z
        self.coord=Vecteur3D(self.x,self.y,self.z)
        self.dist=dist
        
        #scores
        self.pa= prob_angle
        self.pd= prob_dist
        self.pt= prob_tot
        self.pm= prob_main
        #nom
        self.nom=nom
        self.couleur=couleur
        self.taille=taille
        self.activation=activation # valeur d'activation pour l'algorithme par activation
        self.reconnu=reconnu
    # getters et setters   
    def setpa (self, new_prob):
        self.pa= new_prob
        
    def setpd (self, new_prob):
        self.pd= new_prob
        
    def setpt (self, new_prob):
        self.pt= new_prob
        
    def setpm (self, new_prob):
        self.pm= new_prob
        
    def getpa (self):
        return self.pa
    def getpd (self):
        return self.pd
    def getpt (self):
        return self.pt
    def getpm (self):
        return self.pm  
    def getcouleur(self):
        return self.couleur
    
    
        
    def __str__(self):
        return("Sphère ("+self.nom+"," \
		+str(self.coord)+ "," \
        +str(self.pa)+ "," \
        +str(self.pd)+ "," \
        +str(self.pm)+ "," \
		+str(self.pt)+ ")")
      
    def __repr__(self):
        return("Sphère ("+self.nom+"," \
		+str(self.coord)+ "," \
        +str(self.prob_angle)+ "," \
        +str(self.prob_dist)+ "," \
        +str(self.prob_main)+ "," \
		+str(self.prob_tot)+ ")")