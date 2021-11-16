#!/usr/bin/env python3

import random
import math
import time
import copy
import numpy as np
import matplotlib.pyplot as plt

import cell
import tissue

random.seed(time.time()) #To get a "really" random generator 


default_clone_init = {0: {"fitness" : 1,"mu": 0.001, "freq" : 0}}

def run (nb_runs, omega, alpha, T, treatment = True, verbose = True, clones_init=default_clone_init):
    
    my_tissue = tissue.Tissue(omega, alpha, T, clones_init=clones_init)
    my_tissue.initial_population(N = 1000, prop_cancer = 0.1)  #initial population of 1000 individus
    
    if verbose:
        print("Initilisation : ")
        print ( "Total number of cells : {}, number of normal cells : {}, number of cancerous cells {}".format(my_tissue.stats()[0], my_tissue.stats()[1], my_tissue.stats()[2]) ) 

    for i in range (nb_runs):
        my_tissue.reproduce()
        my_tissue.get_apoptose()
        
        if (treatment) :
            my_tissue.get_treatment()
        
        nb_cells, nb_normal_cells, nb_cancer_cells = my_tissue.stats()
        
    for key in list(my_tissue.clones_pop.keys()):
        if (key != 0 and my_tissue.clones_pop[key]["freq"] == 0):
            del my_tissue.clones_pop[key]
    
    if verbose :
        print ( "Statistics after", nb_runs, "runs : ")
        print ( "Total number of cells : {}, number of normal cells : {}, number of cancerous cells : {}".format(nb_cells, nb_normal_cells, nb_cancer_cells, "\n" ) )
        print ( "\n" )
        #print(my_tissue.clones_pop)
    return (my_tissue.stats())

if __name__ == "__main__" :
	
	print("simulation")
