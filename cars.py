cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")

print(sorted(cars)) #Temporarily sort

#reverse the list
print("\nHere is the reversed list:")
cars.reverse()
print(cars)

numberofcars = len(cars)
print("\nThere are " + str(numberofcars) + " cars in the list.")


#Sort the list
cars.sort()
print(cars)
