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
	'''
	This function generates three pseudo-random numbers and returns the lowest of three for medium mode, the middle for hard mode and the highest for unfair mode	
	'''
	three_rand_numbers = [ random_gen.random_01_gen(), random_gen.random_01_gen(), random_gen.random_01_gen() ]
	if difficulty == 0: return 0
	if difficulty == 1: return sorted(three_rand_numbers)[0]
	if difficulty == 2: return sorted(three_rand_numbers)[1]
	if difficulty == 3: return sorted(three_rand_numbers)[2]


def gold_location (dimension):
	'''
	Returns a dictionary which points to the location of gold on the map.

	'''

	gold = [ int(math.floor(random_gen.random_01_gen()*dimension)),int(math.floor(random_gen.random_01_gen()*dimension))]
	#print "gold at "
	#print gold
	return {'gold_location':gold}

def wumpus_location (dimension):
	'''
	Returns a dictionary which has elements:
	the wumpus location
	squares for the location of the stench
	'''


	wumpus_loc = [ int(math.floor(random_gen.random_01_gen()*dimension)),int(math.floor(random_gen.random_01_gen()*dimension))]
	#print "wumpus at "
	#print wumpus_loc
	stench_up = [wumpus_loc[0], wumpus_loc[1] +1]	
	stench_down = [wumpus_loc[0], wumpus_loc[1] -1]	
	stench_left = [wumpus_loc[0]-1, wumpus_loc[1]]	
	stench_right = [wumpus_loc[0]+1, wumpus_loc[1]]	

	stench_loc = [ stench_up, stench_down, stench_left, stench_right ]
	stench_loc = [stench for stench in stench_loc if (stench[0] > -1 and stench[1] > -1)]
	if [0,0] in stench_loc: stench_loc.remove([0,0]) 
	#print stench_loc
	return {'wumpus_location':wumpus_loc, 'stench_location':stench_loc}

def pits_location (dimension,difficulty):
	'''
	Returns a dictionary which has elements 
	num_pits - Number of pits in the map	
	list of locations for the pit as a list of lists [[0,1], [99,45].....]
	list of locations for the breeze as a list of lists	

	'''
	
	num_pits = int(math.floor(dimension * dimension * 0.1 * difficulty_function(difficulty)))
	#print num_pits
	pits = [[0,0] for i in range(num_pits)]
	for i in range(num_pits):
		pits[i] = [ int(math.floor(random_gen.random_01_gen()*dimension)), int(math.floor(random_gen.random_01_gen()*dimension)) ]
	#print "pits at "
	#print pits
	breeze_pl = [[0,0] for i in range(num_pits*4+1)]
	for i in range(num_pits):
		pit_up = [pits[i][0], pits[i][1] + 1]
		pit_down = [pits[i][0], pits[i][1] - 1]
		pit_left = [pits[i][0] - 1, pits[i][1]]
		pit_right = [pits[i][0] + 1, pits[i][1]]
		breeze_pl[4*i] = pit_up
		breeze_pl[4*i+1] = pit_down
		breeze_pl[4*i+2] = pit_left
		breeze_pl[4*i+3] = pit_right
	#print breeze_pl
	breeze_pl = [breeze for breeze in breeze_pl if (breeze[0] > -1 and breeze[1] > -1)]
	if [0,0] in breeze_pl: breeze_pl.remove([0,0]) 
	#for breeze in breeze_pl:
	#	if ((breeze[0] < 0) or (breeze[1] < 0)):
	#		breeze_pl.remove(breeze)
	#print breeze_pl
	pit_return = {'number_pits':num_pits, 'pit_location':pits, 'breeze_location':breeze_pl}
	return pit_return



def world(dimension,difficulty):
	'''
	The world generator
        Dimension : the size of the world is dimension * dimension
	Difficulty : easy - No pits, medium - 1*x pits, hard - 1.5*x pits, unfair - 2*x pits	
	'''
	#Initialise list of percepts: [[loc,loc],
	#Glitter, Stench, Breeze, Scream
	
	percept_var = [[0,0], False, False, False, False] 
	world_var = [[percept_var] for i in range(dimension*dimension)]
	for k in range(dimension):
		for j in range(dimension):
			world_var[k*10+j] = [[k,j], False, False, False, False]
	for i in range(dimension*dimension):
		print i,world_var[i]
	pit_return = pits_location(dimension,difficulty)
	gold_return = gold_location(dimension)
	wumpus_return = wumpus_location(dimension)	
	for breeze in pit_return['breeze_location']:
		for i in range(dimension*dimension):
			if world_var[i][0] == breeze:
				world_var[i][3] = True
				#print i, world_var[i]
				break	
	for stench in wumpus_return['stench_location']:			
		for i in range(dimension*dimension):
			if world_var[i][0] == stench:
				world_var[i][2] = True
				#print i, world_var[i]
				break
	for i in range(dimension*dimension):
		if gold_return['gold_location'] == world_var[i][0]:
			world_var[i][1] = True
			break	
	#for i in range(dimension*dimension):
	#	print i,world_var[i]


#'''
world(10,3)
'''
for i in range(4):
	pits_location (100,i)	
'''	




