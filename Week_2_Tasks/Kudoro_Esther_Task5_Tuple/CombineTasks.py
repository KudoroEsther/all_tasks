#Task 1 Create and Display
dishes = ()
dish1 = input("Enter your favorite Nigerian dishes: ")
dish2 = input("Enter your 2nd favorite Nigerian dishes: ")
dish3 = input("Enter your 3rd favorite Nigerian dishes: ")

dishes = dish1, dish2, dish3 #Assigned the favourite dishes to the tuple called dishes
print(dishes)
print(*dishes, sep="\n") #prints each dish on a new line

#Task 2 Tuple and input
friend = input("Enter 5 of your best friends' names with spaces in between: ").split()
friends = tuple(friend)
print(type(friends))
print(friends[::-1])

#Task 3 Tuple Operations
states = tuple(input("Input five Nigerian states separated by spaces: ").title().split())
print(states[0], states[-1]) #This prints out the first and last states
print("Lagos" in states) #This checks if lagos is in the list called states
print(len(states)) #prints the number of states

#Task 4 Tuple Unpacking
info_tuple = tuple(input("Input the follwing information with spaces in between Firstname, Age: ").split())
color_town = tuple(input("Enter  your favorite color and hometown with space between them: ").split())
name, age = info_tuple
color, town = color_town

print(f"Name: \t\t\t{name} \nAge: \t\t\t{age} \nFavorite color: \t{color} \nHometown: \t\t{town}")

#Task 5 Modify tuple indirectly
shop = input("Enter three shoppoing items with space between them: ").split() #used .split() to convert into words
shopping_list = tuple(shop) #converted the string to tuple and assigned to a variable
ListShop = list(shopping_list) #converted to list
ListShop.extend(["garri", "ferrero"]) #tried using .append() but it only accepts one argument, so I used .extend with a list containing strings
print(ListShop)
shopping_tuple = tuple(ListShop)
print("|".join(shopping_tuple)) #this separates the content of the tuple with |

# Task 6 Attendance tracker
name = input("Enter your namme: ")
gender = input("Enter your gender: ")
course = input("Enter your course track: ")
month_input = int(input("Enter the month number, for example January=1: "))
week_input = int(input("Enter the day number, for example Sunday=1: "))

week = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
month = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
print(type(week))

print(f"Name: {name}")
print(f"Gender: {gender}")

print(f"Month: {month[month_input -1]}") #This is essentially {month[index_number]} where index_number = month_input -1

#This selects the day of the week with an index number that is equal to the inputted number-1. For example, if week_input = 2, the output will be an element with an index number of 2-1, which is Monday in this case.
print(f"Week:  {week[week_input -1]}")