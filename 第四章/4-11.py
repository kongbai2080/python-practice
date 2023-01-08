pizzas = ['apple','pineapple','peach']
for pizza in pizzas:
	print("I like " + pizza + " pizza")
print("I really like pizza")	
friend_pizzas=pizzas[:]
pizzas.append("bean")
friend_pizzas.append('onion')
print("My favourite pizza are:")
print(pizzas)
for pizza in pizzas:
	print(pizza)
print("My friend's favourite pizza are:")
print(friend_pizzas)
for pizza in pizzas:
	print(pizza)	
