users = []
#users = ["Eric","admin","Tom","Amy","John"]
if users:
	for user in users:
		if user == "admin":
			print("Hello admin,would you like to see a status report?")
		else:
			print("Hello " + user +",thank you for logging it again")
else :
	print("We need to find some users")
