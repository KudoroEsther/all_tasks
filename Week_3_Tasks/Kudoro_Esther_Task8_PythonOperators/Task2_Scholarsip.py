# # #this accepts the user's name
# name = input("Enter your name: ")

# #this accepts the user's age as an integer
# age = int(input("Enter your age: "))

# #this accepts the user's score as an integer
# score = int(input("Enter your test score: "))

# #this checks the eligibility of the user using several logical operators
# eligibility = (age <18) and (score > 70)

# #this prints out the user's details and their eligibility
# print(f"Candidate: {name}\nAge: {age}\nScore: {score}\nEligible: {eligibility}")

"""
The input valiadation section of the code is self explanatory. 
eligibility = (age <18) and (score > 70) checks that the user is older than 18 and has a score greater than 70, this prints True or False depending on the user's input

print(f"Candidate: {name}\nAge: {age}\nScore: {score}\nEligible: {eligibility}") this uses f-string to print out the user's details and the eligibility
"""


# #Adapting the code
# citizen = input("Enter your nationality: ").title()
# enrollment = input("Are you registered full-time undergraduate student of a Nigerian university? Input Yes or No: ").lower()

# scholarship = input("Are you a beneficiary of any other scholarship from an entity in the Oil and Gas industry? Input Yes or No: ").lower()

# qualification = input("Do you have As or Bs in English, Mathematics and any other three sujects in your WAEC/WASSCE exam? Input Yes or No: ").lower()

# eligibility = (age <18) and (score > 70) and (citizen == "Nigerian") and (enrollment == "yes") and (scholarship == "no") and (qualification == "yes")

# print(f"Candidate: {name}\nAge: {age}\nScore: {score}\nEligible: {eligibility}")



# #OR
name = input("Enter your name: ").title()
age = int(input("Enter your age: "))
score = int(input("Enter your test score: "))

subject = ["Maths", "English", "TD", "Chemistry", "Physics"]
grade1 = input(f"Input your grade for {subject[0]}, you can only input A or B: ").upper()
grade2 = input(f"Input your grade for {subject[1]}, you can only input A or B: ").upper()
grade3 = input(f"Input your grade for {subject[2]}, you can only input A or B: ").upper()
grade4 = input(f"Input your grade for {subject[3]}, you can only input A or B: ").upper()
grade5 = input(f"Input your grade for {subject[4]}, you can only input A or B: ").upper()

citizen = input("Enter your nationality: ").title()
enrollment = input("Are you registered full-time undergraduate student of a Nigerian university? Input Yes or No: ").lower()

scholarship = input("Are you a beneficiary of any other scholarship from an entity in the Oil and Gas industry? Input Yes or No: ").lower()

# qualification = (((grade1 == "A") or (grade1 =="B")) and ((grade2 == "A") or (grade2 =="B")) and ((grade3 == "A") or (grade3 =="B")) and ((grade4 == "A") or (grade4 =="B")) and ((grade5 == "A") or (grade5 =="B")) )
# # print(qualification)

# eligibility = (age <18) and (score > 70) and (citizen == "Nigerian") and (enrollment == "yes") and (scholarship == "no") and (qualification == True)

# print(f"Candidate: {name}\nAge: {age}\nScore: {score}\nEligible: {eligibility}")

# #OR
grades = [grade1, grade2, grade3, grade4, grade5]
# list(grades)
# print(grades)

eligibilityy = (age <18) and (score > 70) and (citizen == "Nigerian") and (enrollment == "yes") and (scholarship == "no") and (set(grades) <= {"A","B"})

print(eligibilityy and f"Congratulations {name}! you're eligible for the scholarship" or f"{name} you're not eligible for the scholarship")

