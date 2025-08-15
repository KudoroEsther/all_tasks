#Task 5 Student score tracker
list_names = []
list_scores = []
names = input("Enter three students names: ").split()
list_names.extend(names) #Used extend instead of append because it kept adding names as a nested list
for i in list_names:
    list_scores.extend(input(f"Enter the score for {i}: ").split()) #this accepts scores for each student using a for loop and it adds it to empty list defined earlier

print(f"Name \t\tScore \n{list_names[0]} \t\t{list_scores[0]} \n{list_names[1]}\t\t{list_scores[1]} \n{list_names[2]}\t\t{list_scores[2]}")
