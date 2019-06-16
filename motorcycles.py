motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles.insert(0, 'harley')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(popped_motorcycle)
print(motorcycles)

first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

motorcycles.remove('suzuki')
print(motorcycles)

motorcycles.insert(0, 'honda')
motorcycles.append('ducati')
motorcycles.insert(2, 'suzuki')
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")
