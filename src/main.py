#!/usr/bin/env python3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import time
import copy

import simulation

random.seed(time.time())

N_runs = 10000
nb_init_clones = 3
clones_init = {0: {"fitness" : 1,"mu": 0.001, "freq" : 0}}

for i in range(1,nb_init_clones+1):
    clones_init[i] = clones_init.get(i, {"fitness" :round(random.uniform(0,2), 3), 
                                         "mu": round(random.uniform(0, 0.02), 4), 
                                        "freq" : 0})

#Without treatment :
simulation1 = simulation.run(nb_runs=N_runs, 
                  N=2000, 
                  prop_cancer= 0.1, 
                  treatment=False, 
                  verbose=True,
                  weighted_reproduction = True,
                  weighted_apoptosis = True,
                  init_clones=10)


#With treatment :
simulation2 = simulation.run(nb_runs=N_runs, 
                   N=2000, 
                   prop_cancer=0.1, 
                   omega=0.25, 
                   alpha=0.5, T=10, 
                   treatment=True, 
                   nb_treatments=2, 
                   verbose=True,
                   weighted_reproduction = True,
                   weighted_apoptosis = True,
                   init_clones=10)


if __name__ == "__main__" :
	
	print("main")
