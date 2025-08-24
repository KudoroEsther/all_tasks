#TASK 3
#11 spliting into a list
print("spliting into a list")
fruits = "apple,banana,orange"
print(f"Fruits = {fruits.split()}")

#12 Escape sequence
print("Escape sequence")
sent = input("Please input a sentence: ")
sent2 = "\n".join(sent.split())
print(sent2)

#13 Replacing spaces with underscores
print("Replacing spaces with underscores")
randd = "It's a great day isn't it?"
print(randd.replace(" ", "_"))

#14Counting the number of times a appears in banana
print("Counting the number of times a appears in banana")
word = "banaana"
print(word.count("a"))

#15 Checking if a string starts with "https://"
print("Checking if a string starts with \"'https://'\" ")
string = "https://github.com"
print(string.startswith("https://"))