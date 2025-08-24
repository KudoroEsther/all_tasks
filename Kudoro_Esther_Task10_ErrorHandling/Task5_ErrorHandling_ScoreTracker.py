#Error Handling
names = []
scores = []

try:
    for i in range (1,4): #this runs the loop 3 times
        name = input("Enter the students name: ").strip().title()
        names.append(name) #adds the inputted name to the empty list

        score = float(input(f"Enter {name}'s score: "))
        scores.append(score)
        total= zip(names,scores) #attaches the each score to the right name

    print("Name \tScore")
    for x,y in total: #attaches te contents of names to x and the content of scores to y
        print(f"{x} \t {y}") #this prints out x and y with a tab between them
        # print(f"{scores}")
except ValueError:
    print("Score should be an integer or a decimal.")
except Exception as a:
    print("Error", a)
finally:
    print("Done tracking scores.")