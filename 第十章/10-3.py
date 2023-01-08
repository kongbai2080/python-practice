filename = 'guest_book.txt'
a = ' '
with open(filename, 'a') as file_object:
	while a != "quit":
		if a == "quit":
			break
		else:
			a = input("please input your name: ")
			file_object.write(a + "have log in\n")
			print("Hello, " + a + "!")
