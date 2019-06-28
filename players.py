players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players)

#print a slice of a list
print(players[0:3])

#print up to index 4
print(players[:4])

#print after index 2
print(players[2:])

#print the last 3 items in a list no mater what if the size changes
print(players[-3:])

print("\nHere are the first 3 players on my team:")
for player in players[:3]:
	print(player.title())
