###################
# still in development, a lot of variables are hardcoded
# in it's current state, only allows player to attack the first enemy in a list
# when the player kills that enemy, the next enemy in the list is assigned as the players target


import random
from game_controller import *


# function that separates the player and enemy attacks
def fight_mechanic(player, list_of_enemies):
	
	def player_attack(list_of_enemies):
		# assigns the first enemy in a list of enemies as the current enemy
		current_enemy = list_of_enemies[0]
		
		# currently just acts as a prompt for input from the player
		attack = input('choose your attack: ')
		
		# starting to branch player inputs, currently just have one
		if (attack == '1'):
			# attack currently always hits. Some print statements to check the hits are registering
			print(current_enemy.health)
			print('You punch the zombie')
			current_enemy.health -= 5 
			print('It now has ' + str(current_enemy.health) + ' health left')
			
			# if the player kills the enemy, they are popped from the list. the next enemy then becomes the current enemy
			if (current_enemy.health <= 0):
				list_of_enemies.pop(list_of_enemies.index(current_enemy))
				
			print()
		
		# This is curently just in here to check the enemies' remaining health		
		for i in range(len(list_of_enemies)):
			print(list_of_enemies[i].health)
	
	def enemy_attack(player, list_of_enemies):
		
		# currently gives each enemy in the list an attack and gives them a 50/50 chance of hitting
		# a hit currently doesn't register any damage on the player
		for each in range(len(list_of_enemies)):
			attack = random.randint(1, 6)
			if (attack <= 3):
				print('Hit')
			else:
				print('Miss')
	
	# currently just set to a specific number of goes 
	for goes in range(10):
		
		player_attack(list_of_enemies)
		enemy_attack(player, list_of_enemies)			
	
	
################################
# TESTS THE FUNCTION	
			
fight_mechanic(player, tavern.list_of_enemies)

		
