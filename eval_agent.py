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
grabbed_goal_flag = False
return_flag = False 
list_of_visited_locations = []



agent_location = [0,0]

