#Task 2 Tuple and input
friend = input("Enter 5 of your best friends' names with spaces in between: ").split()
friends = tuple(friend)
print(type(friends))
print(friends[::-1])
