# #Task 4 Name Organizer
names = input("Enter five names separated by spaces: ").split()
#I noticed that if i input the .split() after accepting input, it separates the input into characters instead of words.
names = [name.lower() for name in names]
print(*names ,sep="\n")

#OR
name = input("Enter five names separated by spaces: ").lower().split()
name.sort()
print(*name, sep="\n")
