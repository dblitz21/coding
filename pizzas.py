pizzas = ["plain", "pepperoni", "mushroom", "anchovy", "jalapeno", "extra cheese"]

friends_pizzas = pizzas[:]

pizzas.append("olive")
friends_pizzas.append("pineapple")

for pizza in pizzas:
	print("I like " + pizza.title() + " pizza! \n") 

print("I really love Pizza!")

print("\nMy favorite pizzas are:")
for pizza in pizzas:
	print(pizza.title())
	

print("\nMy friend's favorite pizzas are:")
for pizza in friends_pizzas:
	print(pizza.title())
