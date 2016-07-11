#!/usr/bin/env python3

import genetic_helpers as gh

##########
# DATA

target = "to be or not to be that is the question"
generations = []

##########
## CONFIG

generation_size = 50
survival_rate = .3
mutation_rate = .01
generations = 20

##########
# CODE

# generate first generation
generations.append([])
for i in range(generation_size):
    generations[0].append(gh.generate_phrase(len(target)))        
