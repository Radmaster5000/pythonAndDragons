from classes import *
from enemyspawner import *
import random

def loadScene(location, player):
	currentLocation = location
	currentLocation.characters.append(player)
	list_of_characters = []
	for l in range(0, len(currentLocation.characters)):
		list_of_characters.append(currentLocation.characters[l].name)

	print("You are in " + currentLocation.description + ". You see the " + ', and '.join(list_of_characters))


#####################################################
# CAUTION: LIVE TESTING
# WEAR PROTECTIVE EQUIPMENT
	  
#currentLocation.characters.append(player)
#list_of_characters = []
#for l in range(0, len(currentLocation.characters)):
#	list_of_characters.append(currentLocation.characters[l].name)

#print("You are in " + currentLocation.description + ". You see the " + ', and '.join(list_of_characters))


######################################################
	
#print('there are currently ' + str(len(currentLocation.list_of_enemies)) + ' enemies in ' + currentLocation.name)

#currentLocation.list_of_enemies = spawn_zombies(random.randint(1, 6))
	
#print('there are now ' + str(len(currentLocation.list_of_enemies)) + ' enemies in ' + currentLocation.name)

#for i in range(len(currentLocation.list_of_enemies)):
#	print(currentLocation.list_of_enemies[i].name)

######################################################

play = input("welcome to the game. Press j to play.")
if (play == 'j'):
	loadScene(tavern, player)

play = input("press j again")
if (play == 'j'):
	loadScene(forest, player)

play = input("press j to quit")
if (play == 'j'):
	quit()

