#use for loop to accept students names
#ask for score for each student
#store names and score in list
#print each studnt names and score on a new line
names = []
scores = []

for i in range (1,4): #this runs the loop 4 times
    name = input("Enter the students name: ").strip().title()
    names.append(name) #adds the inputted name to the empty list

    score = float(input(f"Enter {name}'s score: "))
    scores.append(score)
    total= zip(names,scores) #attaches the each score to the right name

print("Name \tScore")
for x,y in total: #attaches te contents of names to x and the content of scores to y
    print(f"{x} \t {y}") #this prints out x and y with a tab between them
    # print(f"{scores}")