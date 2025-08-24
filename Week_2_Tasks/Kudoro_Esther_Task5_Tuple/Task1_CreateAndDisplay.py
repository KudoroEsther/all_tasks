#Task 1 Create and Display
dishes = ()
dish1 = input("Enter your favorite Nigerian dishes: ")
dish2 = input("Enter your 2nd favorite Nigerian dishes: ")
dish3 = input("Enter your 3rd favorite Nigerian dishes: ")

dishes = dish1, dish2, dish3 #Assigned the favourite dishes to the tuple called dishes
print(dishes)
print(*dishes, sep="\n") #prints each dish on a new line