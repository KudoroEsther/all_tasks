# #Task 1 Student biodata storage
# info = {
#     "Name": input("Input your name: "),
#     "age": int(input("Enter your age: ")),
#     "gender": input("Input your gender: "),
#     "course": input("Enter your course: ").split()
# }
# # print(*info.items(), sep="\n")
# for key, val in info.items():
#     print(f"{key}:\t{val}") #prints the content of the dictionary on a new line with tab in between


#Task 2 Super market price list
items_price = {} #defined an empty dictionary
items = ["rice", "beans", "banana"]
items_price["rice"] = float(input(f"Enter the price for {items[0]}: ")) #this accept float input and assigns it to the key rice, indexing is used to display the appropriate item
items_price["beans"] = float(input(f"Enter the price for {items[1]}: "))
items_price["banana"] = float(input(f"Enter the price for {items[2]}: "))

print(items_price.keys())
print(type(items_price))
updated_item = input("Input the name of the item to be updated: ").lower() #this accepts the name of the item to be updated and .lower() is used to prevent error in the next line
if updated_item in items:
    updated_price = float(input(f"Input the new price of the {updated_item}: ")) #if the inputted item is found in items, it accepts a new price
    items_price.update({updated_item:updated_price}) #this updates the price in the main dictionary
else:
    print("Invalid item, try again")
print(items_price) #this prints the updated dictionary


#Task 4 Days and acitvities pairing
week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
act1 = input(f"Input an activity for {week[0]}: ")
act2 = input(f"Input an activity for {week[1]}: ")
act3 = input(f"Input an activity for {week[2]}: ")