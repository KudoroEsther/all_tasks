#Task 4 Tuple Unpacking
info_tuple = tuple(input("Input the follwing information with spaces in between Firstname, Age: ").split())
color_town = tuple(input("Enter  your favorite color and hometown with space between them: ").split())
name, age = info_tuple
color, town = color_town

print(f"Name: \t\t\t{name} \nAge: \t\t\t{age} \nFavorite color: \t{color} \nHometown: \t\t{town}")
