#!/usr/bin/env python3

import random
import time
import simulation

random.seed(time.time()) #To get a "really" random generator 


nb_init_clones = 3
clones_init = {0: {"fitness" : 1,"mu": 0.001, "freq" : 0}}
for i in range(1,nb_init_clones+1):
    clones_init[i] = clones_init.get(i, {"fitness" :round(random.uniform(0,1), 4), 
                                         "mu": round(random.uniform(0, 0.002), 4), 
                                        "freq" : 0})

#Without treatment :
simulation1 = simulation.run(nb_runs=10000, omega=0.25, alpha=0.5, T=25, treatment=False, verbose=True, clones_init=clones_init)


#With treatment :
simulation2 = simulation.run(nb_runs=10000, omega=0.25, alpha=0.5, T=25, treatment=True, verbose=True, clones_init=clones_init)


if __name__ == "__main__" :
	
	print("main")
