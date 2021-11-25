#!/usr/bin/env python3

import numpy as np
import random
import time
import copy

class Cell (object) :
   
    next_ID = 0
    
    def __init__(self, state = "NORMAL", clone = 0, fitness = 1, mutation_rate = 0.001):
        self.state = state
        self.fitness = fitness
        self.clone = clone
        self.mutation_rate = mutation_rate
        self.ID = Cell.next_ID
        self.get_cure = False
        self.treatment_duration = 0
        Cell.next_ID += 1
        
    def __str__(self):
        return "Cell #{0} of state : {1} and clone type {2}".format(self.ID, self.state, self.clone)
    
    def mutate (self, new_clone_id):
        if self.state == "NORMAL":
            self.state = "CANCEROUS"
            
        self.clone = new_clone_id
        self.fitness = round(random.uniform(0,2), 3)
        self.mutation_rate = round(random.uniform(0, 0.02), 4)
        
    def treatment (self, alpha):
        self.get_cure == True
        self.fitness = self.fitness * alpha
        self.treatment_duration += 1

if __name__ == "__main__" :
	
	print("cell")
