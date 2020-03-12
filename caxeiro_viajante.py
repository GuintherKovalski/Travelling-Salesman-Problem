#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 15:12:30 2020

@author: guinther
"""

import numpy as np
import pygmo 
from pygmo import *
import matplotlib.pyplot as plt
global count
import time
count=0
x = np.random.rand(30)*100
y = np.random.rand(len(x))*100
plt.scatter(x,y)
order = np.argsort(np.random.rand(len(x)))
distance = []
plt.scatter(x,y,c='black')
for i in range(len(order)):
    if i<len(order)-1:
        distance.append(((x[order[i]] - x[order[i+1]])**2+(y[order[i]] - y[order[i+1]])**2)**0.5)
        plt.plot(x[order[i:i+2]],y[order[i:i+2]],c='r')
    if i ==len(order)-1:
        distance.append(((x[order[i]] - x[order[0]])**2+(y[order[i]] - y[order[0]])**2)**0.5)
        plt.plot(x[order[[0,i]]],y[order[[0,i]]],c='r')
sum(distance)      
        
        
class sphere_function:
    def __init__(self,X,Y):
        #global model
        self.X = X
        self.Y = Y
        self.lower = [0]*len(X) #(w*1.05).tolist()
        self.upper = [100]*len(X) #(w*0.95).tolist() 
       
    def fitness(self,x):
        global count
        count +=1
        order = np.argsort(x)
        distance = []
        plt.scatter(self.X ,self.Y,c='black')
        for i in range(len(order)):
            if i<len(order)-1:
                distance.append(((x[order[i]] - self.X[order[i+1]])**2+(self.Y[order[i]] - self.Y[order[i+1]])**2)**0.5)
                plt.plot(self.X[order[i:i+2]],self.Y[order[i:i+2]],c='r')
            if i ==len(order)-1:
                distance.append(((self.X[order[i]] - self.X[order[0]])**2+(self.Y[order[i]] - self.Y[order[0]])**2)**0.5)
                plt.plot(self.X[order[[0,i]]],self.Y[order[[0,i]]],c='r')
        if count%300==0:
            plt.savefig('caxeiro/'+str(time.time())+'.png')
            count=0
        plt.clf()
        plt.cla()
        sum(distance)      

        return [sum(distance)   ] 
    def get_bounds(self):
        return ((self.lower),(self.upper))       


m = sphere_function(x,y)
prob1 = pg.problem(m)
algo1 = algorithm(xnes(gen = 1000, eta_mu = 0.2, eta_sigma = 0.1, eta_b = 0.1, sigma0 = 0.1, ftol = 1e-6, xtol = 1e-6, memory = False, force_bounds = True))
algo2 = algorithm(cmaes(gen = 5000,force_bounds = True)) 
algo3 = algorithm(de(gen = 500))
#algo4 = algorithm(algorithm.sga_gray(gen = 20))
algo5 = algorithm(sea(gen = 500))
algo6 = algorithm(bee_colony(gen = 50, limit = 100))
#algo = pg.algorithm(pg.bee_colony(gen = 25, limit = 50))
algo2.set_verbosity(1)
pop = pg.population(prob1,300)
pop = algo2.evolve(pop)
print(pop.champion_f)
p = pop.get_x()[pop.best_idx()] 
order = np.argsort(p)
distance = []
plt.scatter(x,y,c='black')
for i in range(len(order)):
    if i<len(order)-1:
        distance.append(((x[order[i]] - x[order[i+1]])**2+(y[order[i]] - y[order[i+1]])**2)**0.5)
        plt.plot(x[order[i:i+2]],y[order[i:i+2]],c='r')
    if i ==len(order)-1:
        distance.append(((x[order[i]] - x[order[0]])**2+(y[order[i]] - y[order[0]])**2)**0.5)
        plt.plot(x[order[[0,i]]],y[order[[0,i]]],c='r')
sum(distance)      