nums = [num**3 for num in range(1,11)]
for num in nums :
	print(num)	
print("The firsr three items in the list are:")
for num in nums[:3]:
	print(num)
print("Three items from the middle of the list are:")
for num in nums[3:6]:
	print(num)
print("The last three items in the list are:")
for num in nums[-3:]:
	print(num)
