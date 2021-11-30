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
