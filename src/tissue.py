#!/usr/bin/env python3

import numpy as np
import random
import time
import copy

import cell

class Tissue ( object ) :
    
    def __init__(self, omega, alpha, generation_time, clones_init):
        self.generation_time = generation_time
        self.omega = omega
        self.alpha = alpha
        self.cancer_detection = False
        self.current_cure = None
        self.pop = []
        self.clones_pop = copy.deepcopy(clones_init)    
    
    def initial_population(self, N = 1000, prop_cancer = 0.01):
        
        nb_cancer_cells = round(prop_cancer *N)
        
        for i in range(N):
            if (i < nb_cancer_cells) :
                state = "CANCEROUS"
                clone = random.choice(range(1, len(self.clones_pop.keys())))
                
            else :
                state = "NORMAL"
                clone = 0
            
            fitness = self.clones_pop[clone]["fitness"]
            mutation_rate = self.clones_pop[clone]["mu"]  
                
            new_cell = cell.Cell(state, clone, fitness, mutation_rate)
            self.pop.append(new_cell)
            self.clones_pop[clone]["freq"] += 1 
            
    def stats(self):
        nb_cells = len(self.pop)
        nb_normal_cells = self.clones_pop[0]["freq"]
        nb_cancer_cells = nb_cells - nb_normal_cells
        nb_clones = 0
        
        average_fitness = sum([cell.fitness for cell in self.pop])/(nb_cells)
        
        for key in list(self.clones_pop.keys()):
            if (key != 0 and self.clones_pop[key]["freq"] > 0):
                nb_clones +=1
        
        if (nb_cancer_cells >= self.omega * nb_cells):
            self.cancer_detection = True
        else:
            self.cancer_detection = False
 
        return (nb_cells, nb_normal_cells, nb_cancer_cells, nb_clones, average_fitness)
            
    def targeted_treatment(self, n=5):
        
        if (n>len(self.clones_pop)) :
            n = len(self.clones_pop) -1
        
        # if the cancer has been detected and no cure in progress
        if (self.cancer_detection == True and self.current_cure == None):
            
            # find the biggest colonie of mutant clone to treat in prority
            self.current_cure = [clones[0] for clones in sorted({k:self.clones_pop[k] for k in self.clones_pop if k!=0}.items(), 
                                   key=lambda item: item[1]["freq"], 
                                   reverse=True)[:n]]
            
            for cell in self.pop:
                if (cell.clone in self.current_cure):
                    cell.treatment_duration = 0
                    cell.treatment(self.alpha)
                    
        # if there is already a cure on specific clone in progress, just continue it until the end of generation time                
        if(self.current_cure != None):
            remaining_cells_to_treat = 0
            for cell in self.pop:
                if(cell.clone in self.current_cure and cell.treatment_duration < self.generation_time):
                    cell.treatment(self.alpha)
                    remaining_cells_to_treat += 1
            
            if (remaining_cells_to_treat == 0):
                self.current_cure = None
                for cell in self.pop:
                    cell.get_cure == False
                    cell.treatment_duration = 0
                        
    
    def reproduce (self, weighted=True):
    
        if (weighted):
            candidat = random.choices(self.pop, weights=[c.fitness for c in self.pop], k=1)[0]
        else:
            candidat = random.choice(self.pop)

        new_cell = cell.Cell(candidat.state, candidat.clone, candidat.fitness, candidat.mutation_rate)
        
        
        #Proba of mutation : give birth to a new clone type
        proba_mutation = random.uniform(0, 1) 
        if proba_mutation < new_cell.mutation_rate :
            new_clone_id=len(self.clones_pop.keys())
            new_cell.mutate(new_clone_id)
            self.clones_pop[new_cell.clone] = self.clones_pop.get(new_cell.clone, {"fitness" :new_cell.fitness, 
                                         "mu": new_cell.mutation_rate, 
                                        "freq" : 1})
        else:
            self.clones_pop[new_cell.clone]["freq"] += 1
        
        self.pop.append(new_cell)
    
    def get_apoptose(self, weighted = True):
        if (weighted):
            cell = random.choices(self.pop, weights=[1/(c.fitness+0.01) for c in self.pop], k=1)[0]
        else:
            cell = random.choice(self.pop)
            
        self.pop.remove(cell)
        self.clones_pop[cell.clone]["freq"] -= 1 


if __name__ == "__main__" :
	
	print("tissue")
