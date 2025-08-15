#Task 2 Unique name collector
names = set()
name = input("Enter the name of the people who will be attending the seminar: ").title()
names= set(name.split())
print(sorted(names))
