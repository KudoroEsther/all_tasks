#TASK 1
#1) Displaying in uppercase
rand = input("Input a random phrase: ")
print(rand.upper()) #This prints out the input in uppercase

#2) printing the first and last character of  "python"
randd = "python"
print(f"{randd[0]} {randd[-1]}")

#3)  printing Hello!
name = input("Please input your name: ")
print(f"Hello {name}!")

#4) counting the number of characters in a string without using len
text = "What a day this is"
character = 0
for char in text:
    character += 1
print(character)

#5) Replacing Word with Python
text ="Hello World"
print(text.replace("World", "Python"))


#TASK 2
#6) checking if a string contain the substring 'Python'
text = "Contemplating including python in this or not, also python is case sensitive"
print("python" in text)

#7) Reversing a string
rgreet = reversed("Hello how are you doing?")
rev_greet = "".join(rgreet)
print(rev_greet)

#8) Removing extra spaces
text = " Hi, it's nice to finally meet you "
print(text.strip())

#9 print vowels
sent = input("Please enter a sentence: ").lower()
vowel_o = sent.count("o")
vowel_i = sent.count("i")
vowel_u = sent.count("u")
vowel_e = sent.count("e")
vowel_a = sent.count("a")
total = vowel_o + vowel_i + vowel_u + vowel_e + vowel_a
print(total)

#10 Converting string to int
string = "1234"
mult = int(string)
print(mult*2)


#TASK 3
#11 spliting into a list
fruits = "apple,banana,orange"
print(f"Fruits = {fruits.split()}")

#12 Escape sequence
sent = input("Please input a sentence: ")
sent2 = "\n".join(sent.split())
print(sent2)

#13 Replacing spaces with underscores
randd = "It's a great day isn't it?"
print(randd.replace(" ", "_"))

#14Counting the number of times a appears in banana
word = "banaana"
print(word.count("a"))

#15 Checking if a string starts with "https://"
string = "https://github.com"
print(string.startswith("https://"))