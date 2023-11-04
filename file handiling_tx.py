# open and close it manually
#file=open('text.txt')
#print(list(file))
#file.close()

# open and close it automatically
#with open('text.txt')as file:
#	print(file.read())

#write some file
#with open('new_file.txt','w') as file:
#	file.write('\nhave a great day ahead')

# exercise
with open ('tree.txt','w') as tree_file:
	tree_string=''' x
	 xxx
	xxxxx
	  x
	  x
	  x
	'''
	tree_file.write(tree_string)