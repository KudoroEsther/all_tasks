#Compulsory Task
#Student info
name = input("Input your full name: ").title()
age = int(input("Input your age: "))
gender = input("Input your gender: ").title()
hobby = input("Enter two hobbies separated by commas: ").title().split(",")
hobby_set = set(hobby)
# print(hobby_set)

# #Guardian info
guard_name = input("Enter your guardian's name: ").title().split(" ") #used .split() in order to make dictionary comprehension seamless, without .split(), the output of the comprehension was scattered
guard_nums = input("Enter your guardian's phone number: ").split(" ")

#Subject info
subject = ("English", "Maths", "TD")
score1 = float(input(f"Enter the score for {subject[0]}: ")) #this accepts the score for the specified subject using indexing
score2 = float(input(f"Enter the score for {subject[1]}: "))
score3 = float(input(f"Enter the score for {subject[2]}: "))
scores = (score1,score2,score3) #this assigns the contents of the three variables to a single variable

# #pairing subject with score using dict comprehension, not necessary
# subject_score = dict(zip(subject,scores))
# print(subject_score)

# #average of the scores
average = sum(scores)/len(scores)
# print(f"The average score for the subjects is {average}")
# # print(scores)


#Nested Dictionaries
profile = {
    "Student info":{
        "Name": name,
        "Age": age,
        "Gender": gender,

    },

    "Academics":{
        subject: scores for subject,scores in  zip(subject,scores)
    },

    "Guardian":{
        "G_name": guard_name,
        "G_number": guard_nums
    },
    "Hobbies": list(hobby_set)
}

#Updating the nested dictionary
#Initials
profile["Student info"]["Initials"] = [i[0] for i in name.split(" ")] #this extracts the initials of the inputted name and adds it to the nested dictionary
#Average
profile["Academics"]["Average"] = average
#Number of hobbies
profile["Hobby Count"] = len(hobby_set)


#Output
print("STUDENT PROFILE".center(100,".")) #used .center() to centralize STUDENT PROFILE
print(f"Name: \t\t{profile["Student info"]["Name"]}") #this prints out the value for the key "Name" from the dictionary "Student info" which is nested within "profile"
print(f"Age: \t\t{profile["Student info"]["Age"]}")
print(f"Gender: \t{profile["Student info"]["Gender"]}")
print(f"Initials: \t{profile['Student info']["Initials"]}\n")

print("ACADEMIC PROFILE".center(100,"."))
print(f"Academics: \t\t{profile["Academics"]}")
print(f"Average score: \t\t{profile["Academics"]["Average"]}\n")

print("GUARDIAN INFO".center(100,"."))
print(f"Guardian's Name: \t\t\t{profile["Guardian"]["G_name"]}\n")
print(f"Guardian's Phone number: \t\t{profile["Guardian"]["G_number"]}\n")

print("HOBBY INFO".center(100,"."))
print(f"Hobbies: \t\t\t{profile["Hobbies"]}")
print(f"Total number of hobbies: \t{profile['Hobby Count']}")
