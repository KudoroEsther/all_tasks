#1) Displaying in uppercase
print("Displaying in uppercase")
rand = input("Input a random phrase: ")
print(rand.upper()) #This prints out the input in uppercase

#2) printing the first and last character of  "python"
print("printing the first and last character of  python")
randd = "python"
print(f"{randd[0]} {randd[-1]}")

#3)  printing Hello!
print("printing Hello!")
name = input("Please input your name: ")
print(f"Hello {name}!")

#4) counting the number of characters in a string without using len
print("counting the number of characters in a string without using len")
text = "What a day this is"
character = 0
for char in text:
    character += 1
print(character)

#5) Replacing Word with Python
print("Replacing Word with Python")
text ="Hello World"
print(text.replace("World", "Python"))
