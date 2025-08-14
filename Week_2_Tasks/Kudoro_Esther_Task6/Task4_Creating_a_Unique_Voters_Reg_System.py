#Task 4 Create a unique voters registration system

registered_name1 = set()
for i in range(1,6):
    name = input("Enter the voters names: ").title() #Accepts names and convert to title case in order to cover our bases when it comes to membership
    if name in registered_name1: #checks if the inputted name is in the set called registered_name1 and prints the message below
        print("This voter has been registered!")
    else: #else it add the inputted name to the set
        registered_name1.add(name)
    # print(registered_name)
print(len(registered_name1)) #the prints the number of registered voters
