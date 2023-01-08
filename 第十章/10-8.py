filename = 'cats.txt'
try:
	with open(filename) as f_obj:
		contents = f_obj.read()
except FileNotFoundError:
	pass
else:
	print(contents)

filename = 'dogs.txt'
try:
	with open(filename) as f_obj:
		contents = f_obj.read()
except FileNotFoundError:
	print(filename + "was not found!")
else:
	print(contents.count('john'))
