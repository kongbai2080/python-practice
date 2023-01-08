class Restaurant():
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 4
		
	def describe_restaurant(self):
		print("The name of the restaurant is " + self.restaurant_name.title() + ".")
		print("The cuisine restaurant have is " + self.cuisine_type + ".")
	def open_restaurant(self):
		print("The restaurant is opening")
	def set_number_serve(self,num):
		self.number_served = num
		print("The restaurant have served " + str(self.number_served) + " people.")	
	
	def increment_number_served(self):
		self.number_served += 10
		print("The restaurant have served " + str(self.number_served) + " people.")

