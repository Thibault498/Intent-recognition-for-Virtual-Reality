# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 14:11:57 2020

@author: rouss
"""


import math as math
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from utilisateur import utilisateur
from sphere import spheres
from vect3D import Vecteur3D


"""Classe appliquant notre algorithme de reconnaissance à partir des informations de l'utilisateur et des objets"""

class simulation_kppv (object):
    
    def __init__(self,util=utilisateur(), list_obj=[], list_angle=[], list_dist=[], list_main=[] ):
        
        self.util=util #Utilisateur
        self.list_obj=list_obj #Liste des objets
        
        #Liste contenant les angles entre la vue de l'utilisateur, et les vecteurs reliant l'utilisateur aux objets.
        self.list_angle= list_angle 
        
        self.list_main = list_main #Liste de la position de la main par rapport aux objets
        self.list_dist = list_dist #Liste des distances entre l'utilisateur et l'objet
        
        
    def __str__(self):
        return("Simulation ("+str(self.util)+"," \
		+str(self.list_obj)+ ")")
      
    #Calcul de la distance entre l'utilisateur et les objets
    def dist(self):
        self.list_dist=[]
        for i in range (0,len(self.list_obj)):
            vect2=self.list_obj[i]
            vect = self.util.position - vect2.coord
            m=vect.mod()
            self.list_dist.append(m)
            
    def dist_obj(self,objet):
        objet.dist=[]
        for i in range (0,len(self.list_obj)):
            
            vect2=self.list_obj[i]
            vect = objet.coord - vect2.coord
            m=vect.mod()
            if m==0:
                objet.dist.append(1)
            else:   
                objet.dist.append(1/(1+m))
                
            
   
            
    #Calcul des angles entre la vue de l'utilisateur et les vecteurs reliant l'utilisateur aux objets. 
    #On utilise le produit scalaire pour déterminer ces angles.
    def angle(self):
        self.list_angle=[]
        for i in range (0,len(self.list_obj)):
            a=self.list_obj[i]
            vect2= a.coord
            
            vect1= self.util.vect_vue
            vect = vect1 ** vect2
            deno=vect1.mod() * vect2.mod()
            cang= (vect)/(deno)
            ang = math.acos(cang)
            
            self.list_angle.append(ang)
            
    #Méthode permettant de représenter les différents objets, l'utilisateur et la direction de son champ de vision.
    #ATTENTION : La représentation n'est valable que si l'utilisateur est aux coordonnées 0,0,0, et pour 4 objets.
    def show(self):
        lcoordx=[]
        lcoordy=[]
        lcoordz=[]
        name_list=[]
        
        ucx=[self.util.getx(),self.util.vect_vue.get_x()]
        ucy=[self.util.gety(),self.util.vect_vue.get_y()]
        ucz=[self.util.getz(),self.util.vect_vue.get_z()]
        
        for i in range (0,len(self.list_obj)):
           new= self.list_obj[i]
           lcoordx.append(new.x)
           lcoordy.append(new.y)
           lcoordz.append(new.z)
           name_list.append(new.nom)
           
        mpl.rcParams['legend.fontsize'] = 10
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        
        ax.scatter(lcoordx,lcoordy,lcoordz,color=['red','green','black','blue'],label = [['red','green','black','blue'],name_list])
        ax.plot(ucx,ucy,ucz,'r-')
        ax.legend()
    
    
    #Méthode effectuant la simulation
    def simule_kppv (self):
        self.angle()
        list_prob=[]
        #Evaluation des scores des angles. 
        #Nous ne considérons d'abord que les objets se situant entre 10° et 0°. Nous leurs attribuons le score maximum de 1.
        for i in range (0, len(self.list_obj)):
                
            if abs(self.list_angle[i])<=((math.pi)/18) and abs(self.list_angle[i])>=0 :
                new= self.list_obj[i]
                new.setpt(1)
                self.list_obj[i] = new
                
            else :
                new= self.list_obj[i]
                new.setpt(0)
                self.list_obj[i] = new
                
            
            
        # Evaluation des scores des distances.  
        # L'évaluation s'effectue en fonction de la distance entre l'objet testé et l'objet ayant reçu le score maximum,
        # que nous avons précisé ci-dessus. Le score final des objets testé ici est égale à leur score dépendant de la distance.
        
        for i in range (0, len(self.list_obj)):
            new = self.list_obj[i]
            r= new.getpt()
            if r==1 : 
                self.dist_obj(new)
                self.list_obj[i]= new
                
            else :
                new.dist=[]
                self.list_obj[i]= new
                
        
        for i in range (0,len(self.list_obj)):
            new = self.list_obj[i]
            
            if (len(new.dist)>0):
                
                for j in range (0,len(new.dist)):

                    nex=self.list_obj[j]
                    nex.setpt(new.dist[j])
                    self.list_obj[j]=nex
                    print (str(nex.nom),str(nex.pt))
                    
                    
        
        
        #self.show()