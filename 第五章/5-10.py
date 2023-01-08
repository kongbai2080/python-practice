current_users = ["Eric","Admin","Tom","Amy","John"]
new_users = ["Mike","admin","TOM","Jokson","Jame"]
for a in range(0,5):
	new_users[a] = new_users[a].lower()
	new_users[a] = new_users[a].title()
for user in new_users:
	if user in current_users:
		print("You need to write a new name")
	else:
		print(user + " has not been used")

