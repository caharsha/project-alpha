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




def agent_action_return(percept_seq):
	
