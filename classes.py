class character: 
	def __init__(self, type, subtype, name, strength, health, speed, magic, equipment):
		self.type = type
		self.subtype = subtype
		self.name = name
		self.strength = strength
		self.health = health
		self.speed = speed
		self.magic = magic
		self.equipment = equipment
		
class location:
	def __init__(self, address, status, name, characters, list_of_enemies, items, description, possible_directions):
		self.address = address
		self.status = status
		self.name = name
		self.characters = characters
		self.list_of_enemies = list_of_enemies
		self.items = items
		self.description = description
		self.possible_directions = possible_directions
		

#########################################
# CHARACTER LIBRARY

tavern_owner = character('NPC', 'human', 'Tavern Owner', 1000, 1000, 1000, 0, ['large knife'])
player = character('player character', 'player', 'Adventurer', 1000, 1000, 1000, 1000, ['sword', '10 gold'])

#########################################
# LOCATION LIBRARY

tavern = location((3,3), 'idle', 'Tavern', [tavern_owner], [], [], 'a sleepy tavern', [])