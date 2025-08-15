#Task 3 Tuple Operations
states = tuple(input("Input five Nigerian states separated by spaces: ").title().split())
print(states[0], states[-1]) #This prints out the first and last states
print("Lagos" in states) #This checks if lagos is in the list called states
print(len(states)) #prints the number of states