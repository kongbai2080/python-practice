favourite_num = {
	'Cong': [1,2,3],
	'wei': [2,3,4],
	'bin': [3,4,5],
	'bang': [4,5,6],
	'ying': [5,6,7],
	}
print("Cong's favourite num is: " + str(favourite_num['Cong']))
print("wei's favourite num is: " + str(favourite_num['wei']))
print("bin's favourite num is: " + str(favourite_num['bin']))
print("bang's favourite num is: " + str(favourite_num['bang']))
print("ying's favourite num is: " + str(favourite_num['ying']))

print("\n")
for name,nums in favourite_num.items():
	print(name + "'s favourite nums are:")
	for num in nums:
		print("\t" + str(num))
	print("\n")
