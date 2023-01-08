import json
filename = 'favourite_num.txt'

try:
	with open(filename) as f_obj:
		b = json.load(f_obj)
except FileNotFoundError:
	a = input("What is your favourite number? ") 
	with open(filename, 'w') as f_obj:
		json.dump(a, f_obj)
else:
	print("I know your favourite number! It is " + b)

