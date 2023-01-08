while True:
	try:
		first_num = int(input("input the firsr number: "))
		second_num = int(input("input the second number: "))
	except ValueError:
		print("please input number but not string!")
	else:
		print(first_num + second_num)
 	
