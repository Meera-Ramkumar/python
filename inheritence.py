class Monster:
	def __init__(self,health,energy):
		self.health=health
		self.energy=energy
	#methods
	def attack(self,amount):
		print('The monster has attacked!')
		print(f'{amount} damage was dealt')
		self.energy-=20

	def move(self,speed):
		print('The monster has moved')
		print(f'It has a speed of{speed}')

class shark(Monster):
	def __init__(self,speed):
		self.speed =speed
	def bite(self):
		print('The shark has bitten')
#exercise
#create scorpion class that inherits from monster
class scorpion(Monster):
	def __init__(self,poison_damage,scorpion_health,scorpion_energy):
		self.poison_damage=poison_damage
		super().__init__(health=scorpion_health,energy=scorpion_energy)
	def attack(self):
		print('The scorpion has attacked')
		print(f'It has dealt {self.poison_damage} poison_damage')

scorpion=scorpion(poison_damage=50,scorpion_health=20,scorpion_energy=10)
print(scorpion.health)
scorpion.attack()
