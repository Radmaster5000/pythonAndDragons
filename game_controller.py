from classes import *
from enemyspawner import *
import random
	  
tavern = location((3,3), 'idle', 'Tavern', [], [], [], 'A sleepy tavern.', [])

print(tavern.description)
print(tavern.characters)

player = character('player character', 'player', 'Adventurer', 1000, 1000, 1000, 1000, ['sword', '10 gold'])
print('an adventurer walks in')
tavern.characters.append(player)

print(tavern.description)
print('list of characters: ')
for l in range(0, len(tavern.characters)):
	print(tavern.characters[l].name)
	
print('there are currently ' + str(len(tavern.list_of_enemies)) + ' enemies in ' + tavern.name)

tavern.list_of_enemies = spawn_zombies(random.randint(1, 6))
	
print('there are now ' + str(len(tavern.list_of_enemies)) + ' enemies in ' + tavern.name)

for i in range(len(tavern.list_of_enemies)):
	print(tavern.list_of_enemies[i].name)

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
