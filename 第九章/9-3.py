class User():
	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name
		
	def describe_user(self):
		print("The user's first name is: " + self.first_name + ".")
		print("The user's last name is: " + self.last_name + ".")
	def greet_user(self):
		print("Hello, " + self.first_name + "!")

user1 = User("Paul","first")
user1.describe_user()
user1.greet_user()
print("\n")
user2 = User("Alis","second")
user2.describe_user()
user2.greet_user()
print("\n")
user3 = User("Jame","third")
user3.describe_user()
user3.greet_user()
print("\n")
