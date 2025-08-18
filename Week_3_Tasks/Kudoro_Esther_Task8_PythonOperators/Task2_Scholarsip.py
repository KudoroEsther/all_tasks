# #this accepts the user's name
name = input("Enter your name: ")

#this accepts the user's age as an integer
age = int(input("Enter your age: "))

#this accepts the user's score as an integer
score = int(input("Enter your test score: "))

# #this checks the eligibility of the user using several logical operators
# eligibility = (age <18) and (score > 70)

# #this prints out the user's details and their eligibility
# print(f"Candidate: {name}\nAge: {age}\nScore: {score}\nEligible: {eligibility}")

"""
The input valiadation section of the code is self explanatory. 
eligibility = (age <18) and (score > 70) checks that the user is older than 18 and has a score greater than 70, this prints True or False depending on the user's input

print(f"Candidate: {name}\nAge: {age}\nScore: {score}\nEligible: {eligibility}") this uses f-string to print out the user's details and the eligibility
"""

#Adapting the code
citizen = input("Enter your nationality: ").title()
enrollment = input("Are you registered full-time undergraduate student of a Nigerian university? Input Yes or No: ").lower()

scholarship = input("Are you a beneficiary of any other scholarship from an entity in the Oil and Gas industry? Input Yes or No: ").lower()

qualification = input("Do you have As or Bs in English, Mathematics and any other three sujects in your WAEC/WASSCE exam? Input Yes or No: ").lower()

eligibility = (age <18) and (score > 70) and (citizen == "Nigerian") and (enrollment == "yes") and (scholarship == "no") and (qualification == "yes")

print(f"Candidate: {name}\nAge: {age}\nScore: {score}\nEligible: {eligibility}")