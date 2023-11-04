inventory_names=['screws','wheels','metal parts','rubber bits','screwdrivers','wood']
inventory_numbers=[43,12,95,421,23,43]

print(zip(inventory_names,inventory_numbers)) #not so useful

print(list(zip(inventory_names,inventory_numbers)))# paired up in tuple form

for thing in zip(inventory_names,inventory_numbers):
	print(thing)
	print(thing[0])#prints names
	print(thing[1])#prints numbers

for name,number  in zip(inventory_names,inventory_numbers):
	print(name)
	print(number)
	
for name,number  in zip(inventory_names,inventory_numbers):
	print(f'{name} current inventory:{number}') 