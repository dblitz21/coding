guest_list = ["Colonel Mustard", "Professor Plum", "Mr. Green"]
print(guest_list)

guest_list.append("Ms. Scarlet")
guest_list.insert(1, "Mrs White")
guest_list.insert(4, "Mrs Peacock")

print(guest_list)

suspect = guest_list[-1]

print("\n I know who did it... It was " + suspect + " with the Candlestick in the Study!")  
