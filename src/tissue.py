#!/usr/bin/env python3

import random
import time
import copy
import numpy as np

import cell

random.seed(time.time()) #To get a "really" random generator 


class Tissue ( object ) :
    
    def __init__(self, omega, alpha, generation_time, clones_init):
        self.generation_time = generation_time
        self.omega = omega
        self.alpha = alpha
        self.detection = False
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
        
        if (nb_cancer_cells >= self.omega * nb_cells):
            self.detection = True
            
        return (nb_cells, nb_normal_cells, nb_cancer_cells)
            
    def get_treatment(self):
        if (self.detection == True): #if the cancer has been detected
            for cell in self.pop:
                if (cell.state == "CANCEROUS") and (cell.treatment_duration < self.generation_time):
                    cell.treatment(self.alpha)
    
    def reproduce (self):
        minimum = 1
        candidat = self.pop[0]
        proba_selection = random.uniform(0, 1)
        
        for c in self.pop :
            #selection of an individual with a proba proportional to the fitness
            #i.e. minimize the différence between the proba and the fitness
            if (abs( c.fitness - proba_selection) < minimum):
                minimum = abs( c.fitness - proba_selection)
                candidat = c
        
        new_cell = cell.Cell(candidat.state, candidat.clone, candidat.fitness, candidat.mutation_rate)
        
        
        #Proba of mutation : give birth to another clone type
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
    
    def get_apoptose(self):
        cell = random.choice(self.pop)
        self.pop.remove(cell)
        self.clones_pop[cell.clone]["freq"] -= 1 


if __name__ == "__main__" :
	
	print("tissue")
