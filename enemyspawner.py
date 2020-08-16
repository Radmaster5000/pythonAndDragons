from classes import *

def spawn_zombies(number_of_enemies):
	array_of_zombies = []
	for i in range(number_of_enemies):
		zombie = character('enemy', 'zombie', 'undead zombie', 3, 10, 5, 0, [])
		array_of_zombies.append(zombie)
	return array_of_zombies
