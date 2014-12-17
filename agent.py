'''

Harsha Ashokan Copparam

agent_stupid.py

Takes in a percept sequence and returns action.
Has own world representation.



Agent has variables for suspect_pit, suspect_wumpus, safe_square which it fills in as the agent navigates the world.
'''

'''
agent's world perception: [locX,locY],suspect_pit,suspect_wumpus, safe_square
agent picks next move based on new position's safe square in the database
move to said square only if safe
'''
import random_gen
'''
#dim = 100
agent_world_perception = [[['unknown', 'unknown', 'unknown'] for i in range(dim)] for j in range(dim)]
#print agent_world_perception[99]
grabbed_goal_flag = False
return_flag = False
list_of_visited_locations = []
agent_location = [0,0]
'''
def initialize_agent_perception(agent_world_perception, list_of_visited_locations):
	'''
	
	'''
	#global agent_world_perception
	#print len(agent_world_perception[0])
	#global list_of_visited_locations
	agent_world_perception[0][0] = ['no', 'no', 'yes']
	agent_world_perception[0][1] = ['no', 'no', 'yes']
	agent_world_perception[1][0] = ['no', 'no', 'yes']
	list_of_visited_locations.append([0,0])

def agent_action_return(agent_world_perception, list_of_visited_locations, return_flag, grabbed_goal_flag, percept_seq, agent_loc):
	'''
	Returns agent action, current position (to check if the agent thinks that it is at the same place as the eval_agent thinks it is, parameter associated with action (if any) when a percept_seq is given.
	'''
	#global agent_world_perception
	#global grabbed_goal_flag
	#global agent_location
	#global list_of_visited_locations
	#initialize_agent_perception()
	agent_location = agent_loc
	next_agent_location = next_agent_loc(agent_location)
	next_action_location = []	
	glitter = percept_seq[0]
	stench = percept_seq[1]
	breeze = percept_seq[2]
	bump = percept_seq[3]
	scream = percept_seq[4]
	print glitter	
	if (grabbed_goal_flag == True):
		#get back to (0,0)
		print "Checkpoint 1: "
		if(return_flag == False):
			list_of_visited_locations.reverse()
			return_flag == True
		if agent_location in list_of_visited_locations:
			'''
			Our second heuristic for the agent is used when we choose the shortest path to return to the location of origin for extraction. 
			We reason that moving backward and moving left moves us closer to [0.0] from any location in the world. 
			Hence the same heuristic function is employed except with the lower value favored to achieve the intuition.
			'''
			
			list_of_visited_locations.remove(agent_location)
			next_action_location = list_of_visited_locations(0) 
	elif glitter == True:
		print "Checkpoint 0"
		agent_action = 'grab_gold'
		grabbed_goal_flag = 'True'
		print "agent action:", agent_action
		print "grabbed_gold:", grabbed_goal_flag
		return{'agent_action': agent_action, 'agent_location':agent_location}
		
	else: 
		#print "Checkpoint 1"
		if stench == True:
			for n in next_agent_location:
				print "n in stench loop"
				print n
				if(agent_world_perception[n[0]][n[1]][1] != 'no'): 	
					agent_world_perception[n[0]][n[1]][1] = 'maybe'
					print agent_world_perception[n[0]][n[1]]	
		if breeze == True:	
			for n in next_agent_location:
				print "n in breeze loop"
				print n
				if(agent_world_perception[n[0]][n[1]][0] != 'no'): 	
					agent_world_perception[n[0]][n[1]][0] = 'maybe'
					print agent_world_perception[n[0]][n[1]] 	
 		if((breeze != True) and (stench != True)):
			for n in next_agent_location:
				print "n in safe loop"
				print n	
				agent_world_perception[n[0]][n[1]] = ['no', 'no', 'yes']
	#If safe, go to next_agent_loc, the heuristic here is that, for exploration: 
	#moving forward and moving right are better than moving backward and moving left	
	if(next_agent_location == [] and return_flag == False):
		print "There are no moves that explore any unseen territory. Gold unattainable!"
	if(next_agent_location == [] and return_flag == True):
		print "The agent has been extracted successfully from (0,0) after obtaining the gold. "
	#print "Test 3"
	for n in next_agent_location:
		#print n
		#print list_of_visited_locations
		if n not in list_of_visited_locations:
			if agent_world_perception[n[0]][n[1]][2] == 'yes':
				next_action_location.append(n)
				print next_action_location
				break
	if next_action_location == []:
		for n in next_agent_location:
			#print n
			#print list_of_visited_locations
			if n in list_of_visited_locations:
				next_action_location.append(n)
				if(rand_gen.rand_01_gen() > 0.5):
					break
	#print next_action_location
	#print agent_location	
	if next_action_location[0] == agent_location[0] + 1:
		agent_action = 'move_right'
	if next_action_location[0] == agent_location[0] - 1:
		agent_action = 'move_left'	
	if next_action_location[1] == agent_location[1] + 1:
		agent_action = 'move_forward'
	if next_action_location[1] == agent_location[1] - 1:
		agent_action = 'move_backward'
	print agent_action
	return{'agent_action': agent_action, 'agent_location':agent_location}
	'''
	for i in range(dim):
		for j in range(dim):
			print i,j,agent_world_perception[i][j]
	'''
def next_agent_loc(agent_loc):
	
	'''
	This returns as a list the location of the agent for the moves move_forward, move_backward, move_left and move_right

	Adds checks to see if any of these moves will push us out of bounds.
	'''
	
	move_forward_result = [-1,-1]
	move_backward_result = [-1,-1]
	move_left_result = [-1,-1]
	move_right_result = [-1,-1]
	if(agent_loc[1] + 1 <= dim-1):
		move_forward_result = [agent_loc[0], agent_loc[1] +1]
	if(agent_loc[1] - 1 >= 0):
		move_backward_result = [agent_loc[0], agent_loc[1] -1]
	
	if(agent_loc[0] + 1 <= dim-1):
		move_right_result = [agent_loc[0]+1, agent_loc[1]]
	
	if(agent_loc[0] - 1 >= 0):
		move_left_result = [agent_loc[0]-1, agent_loc[1]]
	next_agent_loc = [move_forward_result, move_backward_result, move_left_result, move_right_result]
	next_agent_loc = [x for x in next_agent_loc if x != [-1,-1]]
	'''
	The heuristic employed while exploring the path uses the sum of the coordinates of the location which results from the action. 
	For example, move forward from [4,5] goes to [4,6], which gives a heuristic value of 10, while, move backward from the same square goes to [4,4] which gives a heuristic value of 8. 
	We take the path with the larger heuristic. 
	This essentially favors moving forward and right over backward and left.
	'''
	
	next_agent_loc.sort(key = lambda x:x[1]+x[0], reverse=True)
	print "next agent location"
	print next_agent_loc
	return next_agent_loc


#dim = 100
'''
agent_world_perception = [[['unknown', 'unknown', 'unknown'] for i in range(dim)] for j in range(dim)]
#print agent_world_perception[99]
grabbed_goal_flag = False
return_flag = False 
list_of_visited_locations = []
agent_location = [0,0]

agent_action_return([False, True, False, False, False], [43,99])
'''
