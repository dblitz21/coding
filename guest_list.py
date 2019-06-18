guest_list = ["Colonel Mustard", "Professor Plum", "Mr. Green"]
print(guest_list)

guest_list.append("Ms. Scarlet")
guest_list.insert(1, "Mrs White")
guest_list.insert(4, "Mrs Peacock")
guest_list.append("Mr. Boddy")

print(guest_list)
numberofguests = len(guest_list)
print("\nThere are " + str(numberofguests) + " guests at the party.")

victim = guest_list.pop()
print("\n " + victim + " has left the party." + "\n")
numberofguests = len(guest_list)

print("There are now " + str(numberofguests) + " guests at the party.\n")
print(guest_list) 



suspect = guest_list[-1]

print("\n I know who did it... It was " + suspect + " with the Candlestick in the Study!")  
