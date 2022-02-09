# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 15:54:26 2020

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

class simulation (object):
    
    def __init__(self,util=utilisateur(), list_obj=[], list_angle=[], list_dist=[] ,list_main=[] ):
        
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
            self.list_dist.append(1/(1+m))
            
    #Calcul de la distance entre la main et les objets       
    def dist_main(self):
        for i in range (0,len(self.list_obj)):
            vect2=self.list_obj[i]
            vect = vect2.coord - self.util.main
            m=vect.mod()
            self.list_main.append(m)
            
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
    def simule (self):
        self.angle()
        self.dist()
        list_prob=[]
        
        
        #Evaluation des scores des angles. 
        #Nous nous basons sur les différentes zones du champ de vision, de la vision périphérique à la vision centrale.
        for i in range (0, len(self.list_obj)):
            
            if abs(self.list_angle[i])> ((math.pi)/3) :
                #Mise à jour du score de chaque objet.
                new= self.list_obj[i]
                new.setpa(0)
                self.list_obj[i] = new
            
            if abs(self.list_angle[i])<=((math.pi)/3) and abs(self.list_angle[i])> ((math.pi)/6) :
                new= self.list_obj[i]
                new.setpa(0.2)
                self.list_obj[i] = new
                
            if abs(self.list_angle[i])<=((math.pi)/6) and abs(self.list_angle[i])> ((math.pi)/9) :
                new= self.list_obj[i]
                new.setpa(0.4)
                self.list_obj[i] = new
                
            if abs(self.list_angle[i])<=((math.pi)/9) and abs(self.list_angle[i])> ((math.pi)/18) :
                new= self.list_obj[i]
                new.setpa(0.6)
                self.list_obj[i] = new
                
            if abs(self.list_angle[i])<=((math.pi)/18) and abs(self.list_angle[i])> ((math.pi)/36) :
                new= self.list_obj[i]
                new.setpa(0.8)
                self.list_obj[i] = new
                
            if abs(self.list_angle[i])<=((math.pi)/36) and abs(self.list_angle[i])>= 0 :
                new= self.list_obj[i]
                new.setpa(1)
                self.list_obj[i] = new
                
        #Prise en compte de la couleur        
        for i in range (0,len(self.list_obj)):
            new=self.list_obj[i]
            if new.couleur == 'red' :
                N = new.getpa()
                M = N + N/10
                new.setpa(M)
            if new.couleur == 'blue' :
                N = new.getpa()
                M = N + N/20
                new.setpa(M)
            if new.couleur == 'black' :
                N = new.getpa()
                M = N + N/10
                new.setpa(M)
            if new.couleur == 'yellow' :
                N = new.getpa()
                M = N - N/10
                new.setpa(M)
        #Prise en compte de la taille       
        for i in range (0,len(self.list_obj)):
            new=self.list_obj[i]
            if new.taille > 0.6 and new.taille <= 0.8 :
                N = new.getpa()
                M = N + N/10
                new.setpa(M)
            if new.taille > 0.8 and new.taille <= 1 :
                N = new.getpa()
                M = N + 2*N/10
                new.setpa(M)
            if new.taille < 0.4 and new.taille >= 0.2 :
                N = new.getpa()
                M = N - N/10
                new.setpa(M)
            if new.taille < 0.2 and new.taille >= 0 :
                N = new.getpa()
                M = N - 2*N/10
                new.setpa(M)
            
        # Evaluation des scores des distances.   
        for i in range (0, len(self.list_obj)):
            new = self.list_obj[i]
            new.setpd(self.list_dist[i])
            self.list_obj[i]= new
            
        #Calcul du score total de chaque objet. Nous appliquons un coefficient 2 à celui de la vue, et de 1 à la distance.
        #Puis nous effectuons la moyenne des deux scores pour déterminer le score total.
        for i in range (0, len(self.list_obj)):
            new = self.list_obj[i]
            a= new.getpa()
            b= new.getpd()
            prob_tot= (4*a +1*b)/5
            new.setpt(prob_tot)           
            
            self.list_obj[i]= new            
            
            print (str(new.nom),str(new.pt))
            list_prob.append(prob_tot)
        
        return list_prob
        #self.show()
            