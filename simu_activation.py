# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 16:07:27 2020

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

class simulation_activation (object):
    
    def __init__(self,util=utilisateur(), list_obj=[], list_angle=[], list_dist=[], list_main=[] ):
        
        self.util=util #Utilisateur
        self.list_obj=list_obj #Liste des objets
        
        #Liste contenant les angles entre la vue de l'utilisateur, et les vecteurs reliant l'utilisateur aux objets.
        self.list_angle= list_angle 
        
        self.list_main = list_main #Liste de la position de la main par rapport aux objets
        self.list_dist = list_dist #Liste des distances entre l'utilisateur et l'objet
        self.k=0 #Variable utilisée pour évaluer l'évolution de la distance entre l'utilisateur et une cible
        
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
            
   
    #Calcul de la distance entre 2 cibles        
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
            if cang > 1 :
                cang = 1
            
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
    def simule_activation (self):
        
    
        #Calcul des angles et des distances
        self.angle()
        self.dist()
            
        #Evaluation des scores des angles. 
        for i in range (0, len(self.list_angle)):
            var = self.list_dist[i] 
            new= self.list_obj[i]
            new.dist=[]
                
            
            # Nous ne considérons d'abord que les objets se situant entre 10° et 0°. 
            if abs(self.list_angle[i])<=((math.pi)/18) and abs(self.list_angle[i])>=(0) :
                new= self.list_obj[i]
                r= new.getpt()
                v=self.k
                self.k= self.list_dist[i]
                #Test pour voir si un objet est activé
                if new.activation == 1 :
                    new.setpt(1)
                    print(str(new.nom),new.getpt())
                    self.dist_obj(new)
                    new.reconnu = 1
                    self.list_obj[i]= new
                    
                else :
                    
                    if self.k < (2*v/3) :  # Cas où l'utilisateur se rapproche de la cible 
                        r = r + 0.02 # Calcul du score au temps t.
                        new.setpt(r)
                        self.dist_obj(new)
                        new.reconnu=1# Variable utilisée pour faciliter l'attribution des scores.
                        self.list_obj[i]= new
                        
                    elif r>=1 : # Si le score de l'objet est de 1, il ne peut plus augmenter
                        new.setpt(r)
                        self.dist_obj(new)
                        new.reconnu=1
                        self.list_obj[i]= new
                        
                    else:
                        r = r + 0.0075 # Augmentation normale du score
                        new.setpt(r)
                        self.dist_obj(new)
                        new.reconnu=1
                        self.list_obj[i]= new
                        
            else:
                new.reconnu=0
                self.list_obj[i]= new
                    
                    
        # Calcul du score des autres objets
        for i in range (0,len(self.list_obj)):
            new = self.list_obj[i]
                
            if (len(new.dist)>0):
                    
                for j in range (0,len(new.dist)):
                    base = new.getpt()
                    nex = self.list_obj[j]
                    r = nex.getpt()
                    re= nex.reconnu
                    if re ==1 :
                        print('')
                    else :   
                        nex.setpt(new.dist[j]*base)
                    #Activation des objets
                    if (nex.getpt()) >=0.5:
                        nex.activation = 1 
                        print(str(nex.nom), 'activée')
                    else: 
                        nex.activation = 0
                            
                    self.list_obj[j] = nex
                    print (str(nex.nom),str(nex.pt))
                       
                        
            
            
            
           
        #self.show()