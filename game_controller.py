from classes import *
from enemyspawner import *
import random
	  
currentLocation = tavern
currentLocation.characters.append(player)
list_of_characters = []
for l in range(0, len(currentLocation.characters)):
	list_of_characters.append(currentLocation.characters[l].name)

print("You are in " + currentLocation.description + ". You see the " + ', and '.join(list_of_characters))



print('another adventurer walks in')
currentLocation.characters.append(player)

	
print('there are currently ' + str(len(currentLocation.list_of_enemies)) + ' enemies in ' + currentLocation.name)

currentLocation.list_of_enemies = spawn_zombies(random.randint(1, 6))
	
print('there are now ' + str(len(currentLocation.list_of_enemies)) + ' enemies in ' + currentLocation.name)

for i in range(len(currentLocation.list_of_enemies)):
	print(currentLocation.list_of_enemies[i].name)

######################################################
# ENEMIES TEST

#list_of_enemies = []
#print(list_of_enemies)
#print()

#for i in range(0, 6):
#	zombie = character('enemy', 'zombie', 'undead zombie', 3, 10, 5, 0, [])
	
#	list_of_enemies.append(zombie)
	
	
#for e in list_of_enemies:
#	print(e.health)
#	print()
	
#list_of_enemies[3].health -= 6

#for e in list_of_enemies:
#	print(e.health)
#	print()

##############################################
