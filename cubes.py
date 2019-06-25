
#Get the cube of the first 10 numbers
cubes = []
for value in range(1, 11):
	cubes.append(value**3)

print(cubes)

#Get the cube of the first 10 numbers shorthand (list comprehension)
cubes2 = [value**3 for value in range(1, 11)]
print(cubes2)
