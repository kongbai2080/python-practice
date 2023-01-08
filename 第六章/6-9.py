favourite_places = {'jingwei':['beijing','shanghai','newyork'],
	'changying':['jinan','guizhou','huizhou'],
	'weihang':['chongqin','jian','huizhou'],
	}
for name,places in favourite_places.items():
	print(name + "'s favourite places are: ")
	for place in places:
		print(place)
	print("\n")
