
# Print a range of numbers
for value in range(1, 6):
	print(value)

print("\n")

# Add a range of numbers to a list
numbers = list(range(1, 6))
print(numbers)

print("\n")

# Print a range of even numbers
even_numbers = list(range(2, 11, 2))
print(even_numbers)

print("\n")

# Print Square Roots
squares = []
for value in range(1, 11):
	squares.append(value**2)

# One line code for squares
#squares = [value**2 for value in range(1, 11)]

print(squares)

print("\n")

# Minumum, Maximum and Summation
digits = []
for value in range(1, 10):
	digits.append(value)
digits.append(0)
print(digits)

print(min(digits))
print(max(digits))
print(sum(digits))


