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


my_restaurant = Restaurant("jukelou", "zhongcai")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
print(my_restaurant.number_served)
my_restaurant.set_number_serve(100)
my_restaurant.increment_number_served()

class IceCreamStand(Restaurant):
	def __init__(self,restaurant_name,cuisine_type):
		super().__init__(restaurant_name,cuisine_type)
		self.flavors = ["chocolate","fruits","butter"]
	
	def describe_flavors(self):
		print(self.flavors)	
		
icecreamstand = IceCreamStand("haoyouduo","ice_cream")
icecreamstand.describe_flavors()
