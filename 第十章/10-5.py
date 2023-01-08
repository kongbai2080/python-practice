filename = 'guest_reason.txt'
a = ' '
with open(filename, 'a') as file_object:
	while a != 'quit':
		if a == 'quit':
			break
		else :
			a = input("Why do you like programming? ")
			file_object.write(a + "\n")
			
		
