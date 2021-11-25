#!/usr/bin/env python3

import numpy as np
import pandas as pd
import random
import time
import copy

import cell
import tissue

default_clone_init = {0: {"fitness" : 1,"mu": 0.001, "freq" : 0}}

def run (nb_runs=10000, N=1000, prop_cancer=0.1, omega=0.2, alpha=0.5, T=20, treatment = True, nb_treatments = 5, verbose = True, weighted_apoptosis = True, clones_init=default_clone_init):
    
    my_tissue = tissue.Tissue(omega, alpha, T, clones_init=clones_init)
    my_tissue.initial_population(N, prop_cancer)  #initial population of 1000 individus
    
    if verbose:
        print("Initilisation : ")
        print ( "Total number of cells : {}, number of normal cells : {}, number of cancerous cells {}".format(my_tissue.stats()[0], my_tissue.stats()[1], my_tissue.stats()[2]) ) 
        print ( "\n" )
        
    nb_cells = []
    nb_normal_cells = []
    nb_cancer_cells = []
    nb_clones = []
    averages_fitness = []
    
    for i in range (nb_runs):
        random.seed(time.time())
        my_tissue.reproduce()
        my_tissue.get_apoptose(weighted_apoptosis)
        
        if (treatment) :
            my_tissue.targeted_treatment(n=nb_treatments)
        
        nb_cells.append(my_tissue.stats()[0])
        nb_normal_cells.append(my_tissue.stats()[1])
        nb_cancer_cells.append(my_tissue.stats()[2])
        nb_clones.append(my_tissue.stats()[3])        
        averages_fitness.append(my_tissue.stats()[4])
    
    df = pd.DataFrame({"Total cells" : nb_cells, 
                  "Normal cells" : nb_normal_cells, 
                  "Tumor cells" : nb_cancer_cells, 
                  "Number of clones": nb_clones, 
                  "Average fitness" : averages_fitness, 
                  })
        
    if verbose :
        print ( "Statistics after", nb_runs, "runs : ")
        print ( "Total number of cells : {}, number of normal cells : {}, number of cancerous cells : {}".format(nb_cells[-1], nb_normal_cells[-1], nb_cancer_cells[-1], "\n" ) )
        print ( "\n" )
        
    return (df)

if __name__ == "__main__" :
	
	print("simulation")
