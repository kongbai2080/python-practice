class Restaurant():
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		
	def describe_restaurant(self):
		print("The name of the restaurant is " + self.restaurant_name.title() + ".")
		print("The cuisine restaurant have is " + self.cuisine_type + ".")
	def open_restaurant(self):
		print("The restaurant is opening")

my_restaurant = Restaurant("jukelou", "zhongcai")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

his_restaurant = Restaurant("bulanni", "xiaochi")
his_restaurant.describe_restaurant()

her_restaurant = Restaurant("yilelamian", "ribenliaoli")
her_restaurant.describe_restaurant()
