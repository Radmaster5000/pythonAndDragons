def build_world (n):
	world = []
	# for each row, create a dictionary
	for i in range(0, n):
		world.append({})
		for j in range(0, n):
			# initialise every space as EMPTY
			world[i].update({j : empty})
	return world
	
		
			
empty = "0"				
print(build_world(6))	
		
		
			
