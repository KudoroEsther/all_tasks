#Task 5 Modify tuple indirectly
shop = input("Enter three shoppoing items with space between them: ").split() #used .split() to convert into words
shopping_list = tuple(shop) #converted the string to tuple and assigned to a variable
ListShop = list(shopping_list) #converted to list
ListShop.extend(["garri", "ferrero"]) #tried using .append() but it only accepts one argument, so I used .extend with a list containing strings
print(ListShop)
shopping_tuple = tuple(ListShop)
print("|".join(shopping_tuple)) #this separates the content of the tuple with |

