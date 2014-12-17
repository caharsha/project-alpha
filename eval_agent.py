'''

Harsha Ashokan Copparam

eval_agent.py

The interface between the agent and the world generated.
Tracks agent's position in the world.
Gives him the percepts appropriate for each move.


'''

import world_gen
import agent_world_interface
import agent




#Defining a world to be used globally for function calls.
envi = world_gen.world_func(100,3)
#Has arrow parameter checks if the agent has used his arrow already.
has_arrow = True
dim = envi['dimension']
#rand_return_var = agent_world_interface.return_percept_seq(envi,'move_forward', [0,99], '',True)


#defining some globals for the agent:
agent_world_perception = [[['unknown', 'unknown', 'unknown'] for i in range(dim)] for j in range(dim)]
return_flag = False
grabbed_gold_flag = False
percept_seq = [False,False,False,False,False]
agent_loc = [0,0]
list_of_visited_locations = []



agent_location = [0,0]
def evaluate_agent():
	#Initialize agent perception
	global envi
	global agent_world_perception
	global return_flag
	global list_of_visited_locations
	global grabbed_gold_flag
	for i in range(100000):
		percept_ret = agent_world_interface.return_percept_seq (envi, agent_act, agent_loc, has_arrow)
		percept_seq = percept_ret['percept_sequence']
		agent_new_pos = percept_ret['agent_new_position']
		agent.initialize_agent_perception(agent_world_perception, list_of_visited_locations)
		#def agent_action_return(agent_world_perception, list_of_visited_locations, return_flag, grabbed_goal_flag, percept_seq, agent_loc):
		agent_ret = agent.agent_action_return(agent_world_perception, list_of_visited_locations, return_flag, grabbed_gold_flag, percept_seq, agent_loc)
		agent_act = agent_ret['agent_action']
		agent_lo = agent_ret['agent_location']
		print agent_act, agent_lo
		if percept_ret['error_msg'] == 2:
			print "Wasted arrow"
		if percept_ret['error_msg'] == 3:
			print "No gold at the location"
		if percept_ret['error_msg'] == 5 or percept_ret['error_msg'] == 6:
			print "Dead agent. "
			return False	
		if return_flag == True and agent_loc == [0,0]:
			print "Successful return"
			if grabbed_gold_flag == True:
				print "Got the gold"
	print "No solution to the particular world."
		
