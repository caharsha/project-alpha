'''changing seeds in random number generator python
Harsha Ashokan Copparam
 
world_gen.py
generates wumpus worlds - given dimensions.
location of wumpus
location of pits
location of gold
dead ends
percepts - bump, scream, glitter, breeze, stench

difficulty variable - difficulty

A function return_percept that returns the percept sequence once specified with a location.
'''

import random_gen
import math

def difficulty_function (difficulty):
	
	
	three_rand_numbers = [ random_gen.random_01_gen(), random_gen.random_01_gen(), random_gen.random_01_gen() ]
	if difficulty == 0: return 0
	if difficulty == 1: return sorted(three_rand_numbers)[0]
	if difficulty == 2: return sorted(three_rand_numbers)[1]
	if difficulty == 3: return sorted(three_rand_numbers)[2]

def pits_location (dimension,difficulty):
	'''
	Returns a list of locations for the pit as a list of lists [[0,1], [99,45].....]
	options {0: 'easy', 1: 'medium', 2: 'hard' , 3: 'unfair'}
	'''
	
	num_pits = int(math.floor(dimension * dimension * 0.1 * difficulty_function(difficulty)))
	#print num_pits
	pits = [[0,0] for i in range(num_pits+1)]
	for i in range(num_pits+1):
		pits[i] = [ int(math.floor(random_gen.random_01_gen()*dimension)), int(math.floor(random_gen.random_01_gen()*dimension)) ]
	pit_return = {'numberPits':num_pits, 'pitlocation':pits}
	return pit_return

def breezes_location (pit_return):

	'''
	Returns the list of locations where the percept breeze is true

	'''	
	#breezes_pl = 
	#return breezes_pl
	
	pass

def world(dimension,difficulty):
	'''
	The world generator
        Dimension : the size of the world is dimension * dimension
	Difficulty : easy - No pits, medium - 1*x pits, hard - 1.5*x pits, unfair - 2*x pits	
	'''
	#Initialise list of percepts: [[loc,loc],
	#Bump, Glitter, Stench, Breeze, Scream
	percept_var = [[0,0], False, False, False, False, False] 
	world_var = [[percept_var] for i in range(1,dimension*dimension+1)]
	#print "\n".join([str(x) for x in world_var])
	pit_return = pits_location(dimension,difficulty)
	#print pit_return['numberPits']
	#print pit_return['pitlocation']	

#'''
world(100,1)
'''
for i in range(4):
	pits_location (100,i)	
'''	




