'''
Harsha Ashokan Copparam

File: agent_world_interface.py

Returns the percept sequence after each agent action
{'world':world_var, 'pit': pit_return, 'gold': gold_return, 'wumpus': wumpus_return}
{'number_pits':num_pits, 'pit_location':pits, 'breeze_location':breeze_pl}
{'gold_location':gold}
{'wumpus_location':wumpus_loc, 'stench_location':stench_loc}
'''

#import world_gen
#envi = world_gen.world_func(100,3)
#has_arrow = True

def return_percept_seq (envi, agent_action, agent_position, parameter, has_arrow):
	#global has_arrow
	wrong_action = -1
	dim = envi['dimension']
	agent_new_position = [0,0]
	if(agent_action == 'move_forward'):
		agent_new_position = [agent_position[0], agent_position[1]+1]	
	if(agent_action == 'move_backward'):
		agent_new_position = [agent_position[0], agent_position[1]-1]	
	if(agent_action == 'move_left'):
		agent_new_position = [agent_position[0]-1, agent_position[1]]	
	if(agent_action == 'move_right'):
		agent_new_position = [agent_position[0]+1, agent_position[1]]
	if(agent_action == 'shoot_wumpus'):
		if(has_arrow == False):
			print "You do not have an arrow to shoot the wumpus with. "	
		elif(parameter == envi['wumpus']['wumpus_location']):
			print "Killed the wumpus"
			for i in range(dim*dim):
				if agent_position == envi['world'][i][0]:
					envi['world'][i][5] = True 
		else: 
			print "You wasted your chance, there was no wumpus at that location."
			wrong_action = 2 #"No wumpus at that location" 
		agent_new_position = agent_position
		has_arrow = False
	if(agent_action == 'grab_gold'):
		if(agent_position == envi['gold']['gold_location']):
			print "You got the gold"
		else:
			print "There was no gold there. "
			wrong_action = 3 #"No gold at that location"
		agent_new_position = agent_position
	if((agent_new_position[0] >= dim) or (agent_new_position[1] >= dim) or (agent_new_position[0] <= -1) or (agent_new_position[1] <= -1)):
		#print agent_new_position[0]
		#print agent_new_position[1]
		print "Reached End of Map, take a different route."
		#wrong_action = 4 #"End of Map"
		for i in range(dim*dim):
			if agent_position == envi['world'][i][0]:
				envi['world'][i][4] = True 
		agent_new_position = agent_position
	if(agent_new_position in envi['pit']['pit_location']):
		print "You just went into one of the numerous pits."
	 	wrong_action = 5 #"Death by pit entry"
	if(agent_new_position == envi['wumpus']['wumpus_location']):
		print "You were killed by the wumpus despite putting up a valiant fight. Yeah, right! But seriously, you died to the wumpus."
		wrong_action = 6 #"Death by wumpus"
	for i in range (dim*dim):
		if(envi['world'][i][0] == agent_new_position):
			percept_seq = envi['world'][i][1:]
	print "***********************************************************"
	print agent_action
	print percept_seq
	print wrong_action
	print agent_new_position
	print "***********************************************************"
        return {'percept_sequence':percept_seq, 'error_msg':wrong_action, 'new_position':agent_new_position}



'''
return_percept_seq(envi,'move_forward', [0,99], '',True)
return_percept_seq(envi,'move_backward', [0,1], '',True)
return_percept_seq(envi,'move_left', [1,0], '',True)
return_percept_seq(envi,'move_right', [0,99], '',True)
return_percept_seq(envi,'grab_gold', envi['gold']['gold_location'],'',True)
return_percept_seq(envi,'shoot_wumpus', envi['gold']['gold_location'],envi['wumpus']['wumpus_location'],True)


return_percept_seq(envi,'move_forward', envi['pit']['breeze_location'][0],'',True)
return_percept_seq(envi,'move_backward', envi['pit']['breeze_location'][0],'',True)
return_percept_seq(envi,'move_right', envi['pit']['breeze_location'][0],'',True)
return_percept_seq(envi,'move_left', envi['pit']['breeze_location'][0],'',True)

print envi['wumpus']['wumpus_location'] 
return_percept_seq(envi,'move_forward', envi['wumpus']['stench_location'][0],'',True)
return_percept_seq(envi,'move_backward', envi['wumpus']['stench_location'][0],'',True)
return_percept_seq(envi,'move_right', envi['wumpus']['stench_location'][0],'',True)
return_percept_seq(envi,'move_left', envi['wumpus']['stench_location'][0],'',True)
'''
