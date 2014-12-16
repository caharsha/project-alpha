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
dim = 100
agent_world_perception = [[['unknown', 'unknown', 'unknown'] for i in range(dim)] for j in range(dim)]

def initialize_agent_perception():
	'''
	
	'''
	global agent_world_perception
	agent_world_perception[0][0] = ['no', 'no', 'yes']
	agent_world_perception[0][1] = ['no', 'no', 'yes']
	agent_world_perception[1][0] = ['no', 'no', 'yes']
	

def agent_action_return(percept_seq):
	'''
	Returns agent action, current position (to check if the agent thinks that it is at the same place as the eval_agent thinks it is, parameter associated with action (if any) when a percept_seq is given.
	'''
	global agent_world_perception
	'''
	for i in range(dim):
		for j in range(dim):
			print i,j,agent_world_perception[i][j]
	'''

'''


'''
initialize_agent_perception()
agent_action_return(0)	
