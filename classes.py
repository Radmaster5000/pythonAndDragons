class character: 
	def __init__(self, type, name, strength, health, speed, magic, equipment):
		self.type = type
		self.name = name
		self.strength = strength
		self.health = health
		self.speed = speed
		self.magic = magic
		self.equipment = equipment
		
class location:
	def __init__(self, name, characters, list_of_enemies, items, description):
		self.name = name
		self.characters = characters
		self.list_of_enemies = list_of_enemies
		self.items = items
		self.description = description
		

#########################################
# CHARACTER LIBRARY

tavern_owner = character('NPC', 'Tavern Owner', 1000, 1000, 1000, 0, ['large knife'])
player = character('player character', 'Adventurer', 1000, 1000, 1000, 1000, ['sword', '10 gold'])

#########################################
# LOCATION LIBRARY

forest = location('Forest', [], [], [], 'a spooky forest')
tavern = location('Tavern', [tavern_owner], [], [], 'a sleepy tavern')
