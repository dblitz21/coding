#Tuples lock in the values
dimensions = (200, 50)

print("Original dimensions:")

#Printing a tuple
for dimension in dimensions:
	print(dimension)
	
#Won't work
#dimensions[0] = 250

#Overwriting a tuple
dimensions = (400, 100)

print("\nModified dimensions:")
for dimension in dimensions:
	print(dimension)
