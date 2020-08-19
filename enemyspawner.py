from classes import *

def spawn_zombies(number_of_enemies):
	array_of_zombies = []
	for i in range(number_of_enemies):
		zombie = character('enemy', 'zombie', 'undead zombie', 3, 10, 5, 0, [])
		array_of_zombies.append(zombie)
	return array_of_zombies

def spawn_demons(number_of_enemies):
	array_of_demons = []
	for i in range(number_of_enemies):
		demon = character('enemy', 'monster', 'demon', 10, 20, 10, 5, [])
		array_of_demons.append(demon)
	return array_of_demons
