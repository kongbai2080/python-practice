class User():
	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name
		self.login_attempts = 0
		
	def describe_user(self):
		print("The user's first name is: " + self.first_name + ".")
		print("The user's last name is: " + self.last_name + ".")
	def greet_user(self):
		print("Hello, " + self.first_name + "!")
	def increment_login_attempts(self):
		self.login_attempts += 1
		print(str(self.login_attempts))
	def reset_login_attempts(self):
		self.login_attempts = 0
		print(str(self.login_attempts))
		
user = User("Paul","first")
for i in range(1,6):
	user.increment_login_attempts()
user.reset_login_attempts()

class Privileges():
	def __init__(self,privileges=["can add post",
		"can delete post","can ban user"]):
			self.privileges = privileges
		
	def show_privileges(self):
		print(self.privileges)
		
		
class Admin(User):
	def __init__(self, first_name, last_name):
		super().__init__(first_name, last_name)
		self.privileges = Privileges()
		
	
		
admin = Admin("Jingwei","Deng")
admin.privileges.show_privileges()


