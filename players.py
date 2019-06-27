players = ['charles', 'martina', 'michael', 'florence', 'eli']

#print a slice of a list
print(players[0:3])

print("\nHere are the first 3 players on my team:")
for player in players[:3]:
	print(player.title())
