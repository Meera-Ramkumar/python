class Monster:
	#attributes
	health=90
	energy=40

	def __init__(self,health,energy):
		print('The moster was created')

	#methods
	def attack(self,amount):
		print('The monster has attacked!')
		print(f'{amount} damage was dealt')
		monster.energy -=20
		print(monster.energy)

	def move(self,speed):
		print('The monster has moved')
		print(f'It has a speed of {speed}')

		

monster1=Monster()
monster2=Monster()

