class Monster:
	#attributes
	health=90
	energy=40

	def __init__(self,health,energy):
		print('The monster was created')
		self.health=health
		self.health=energy
	def __len__(self):
		return self.health

	
	def __call__(self):
		return'The monsterwas called'
	def __add__(self):
		return self.health + other

	#methods
	def attack(self,amount):
		print('The monster has attacked!')
		print(f'{amount} damage was dealt')
		monster.energy -=20
		print(monster.energy)

	def move(self,speed):
		print('The monster has moved')
		print(f'It has a speed of {speed}')

		

monster1=Monster(10,20)
monster2=Monster(health=50,energy=100)
print(len(monster1))
print(monster1.health)
print(monster2.health)
print(monster1 + 10)