#TASK 1
#your favourite quote
quote = input("Please input your favourite quote: ")
quotes = quote.title()
print(f'\"{quotes}\"')

#TASK 2 Shopping list master
empty = []
items = input("Enter 3 shopping items one by one with commas in between: ").split()
empty = items.copy()
print(empty)

#Task 3 Word Counter
sent = input("Enter a sentence: ")
sent_list = list(sent.split()) #this converts the inputed sentence to list
print(len(sent_list))

# #Task 4 Name Organizer
names = input("Enter five names separated by spaces: ").split()
#I noticed that if i input the .split() after accepting input, it separates the input into characters instead of words.
names = [name.lower() for name in names]
print(*names ,sep="\n")

#OR
name = input("Enter five names separated by spaces: ").lower().split()
name.sort()
print(*name, sep="\n")

#Task 5 Student score tracker
list_names = []
list_scores = []
names = input("Enter three students names: ").split()
list_names.extend(names) #Used extend instead of append because it kept adding names as a nested list
for i in list_names:
    list_scores.extend(input(f"Enter the score for {i}: ").split()) #this accepts scores for each student using a for loop and it adds it to empty list defined earlier

print(f"Name \t\tScore \n{list_names[0]} \t\t{list_scores[0]} \n{list_names[1]}\t\t{list_scores[1]} \n{list_names[2]}\t\t{list_scores[2]}")


#Task 6 Word Analyzer
word = input("Enter a word: ")
print(f"the inputed word has {len(word)} letters")
print(word.isupper()) #checks if the word is in uppercase
print(word.islower())
print(word.istitle())

#Task 7 List manipulation
cities = ["Lagos", "Abuja", "New York", "Nottingham", "Dublin"]
cities[3] = "Abeokuta"
cities.pop()
cities.insert(0, "Barcelona")
print(cities)