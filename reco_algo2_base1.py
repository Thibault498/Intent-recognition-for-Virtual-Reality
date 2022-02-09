# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 17:49:25 2020

@author: rouss
"""
import csv
import math as math
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

from utilisateur import utilisateur
from sphere import spheres
from vect3D import Vecteur3D
from simulation import simulation
from simu_voisin import simulation_kppv     
from simu_activation import simulation_activation 
                
#Fonction permettant la récupération des données sur un fichier csv          
def getelem(file, i, j):
    with open(file, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        for line in reader :
            if reader.line_num - 1 == i:
                return line[j]

if __name__=="__main__":
    cib0=[]
    cib1=[]
    cib2=[]
    #Récupération des données
    #Emplacement des cibles
    n23 = getelem('01.csv',1,23)
    n24 = getelem('01.csv',1,24)
    n25 = getelem('01.csv',1,25)
        
    n27 = getelem('01.csv',1,27)
    n28 = getelem('01.csv',1,28)
    n29 = getelem('01.csv',1,29)
        
    n31 = getelem('01.csv',1,31)
    n32 = getelem('01.csv',1,32)
    n33 = getelem('01.csv',1,33)
    
    n23=float(n23)
    n24=float(n24)
    n25=float(n25)
    n27=float(n27) 
    n28=float(n28)
    n29=float(n29)
    n31=float(n31)
    n32=float(n32)
    n33=float(n33)
    #Création des cibles
    sphere = spheres (n23,n24,n25, nom="cible 0")
    sphere2 = spheres (n27,n28,n29, nom="cible 1")
    sphere3 = spheres (n31,n32,n33, nom = "cible 2")
    time=[]
    
    #Lancement de la simulation
    for i in range (1,1488):
        
        n1= getelem('01.csv',i,1)
        n1= float(n1)
        time.append(n1)
        
        n3= getelem('01.csv',i,3)
        n4= getelem('01.csv',i,4)
        n5= getelem('01.csv',i,5)
        n7= getelem('01.csv',i,7)
        n8= getelem('01.csv',i,8)
        n9= getelem('01.csv',i,9)

        
        n7=float(n7)
        n8=float(n8)
        n9=float(n9)
        
        
        n3=float(n3)
        n4=float(n4)
        n5=float(n5)
        
    
        thibault= utilisateur (n3,n4,n5,Vecteur3D(n7,n8,n9), Vecteur3D(),nom="Thibault")
        
    
        simu = simulation_kppv (thibault,[sphere,sphere2,sphere3])
        
        simu.simule_kppv()   
        
        cib0.append(sphere.getpt())
        cib1.append(sphere2.getpt())
        cib2.append(sphere3.getpt())
           
            
    print('')
    print('Cible souhaitée : ', getelem('01.csv',3,21))
    print('')        
            
    plt.figure(figsize=(8,6),dpi=120)
    plt.axis([4,26.5,0,1.1])
    plt.grid()
    plt.title('Evolution des scores au cours du temps') 
    
    plt.xlabel('Temps en secondes')
    plt.ylabel('Scores')
        
    plt.plot(time,cib0, label='score cible 0')
    plt.plot(time,cib1,'r' ,label='score cible 1')
    plt.plot(time,cib2,'y' ,label='score cible 2')
            

    plt.legend()    
        
    