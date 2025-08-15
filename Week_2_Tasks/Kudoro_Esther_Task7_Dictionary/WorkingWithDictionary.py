# #CREATING DICTIONARIES
# #Using curly braces
# student = {
#     "name": "Ada",
#     "age": 20,
#     "course": "Computer Science"
# }
# print(student)

# #Using dict() constructor
# student_info = dict(name = "John", age = 25, course = "Maths") #Using quotes to define the key as a string when applying a dict() constructor leads to errors
# print(student_info)

# #Empty dictionary
# empty_dict = {}
# print(empty_dict)


# #DICTIONARY COMPREHENSION
# #Create a dictionary of numbers and their squares
# squares = {x: x**2 for x in range (1,6)} #defined the key as x and the value as the square of x, then iterated x over a range of 6
# print(squares)

# #With condition
# evens_cube = {x: x**3 for x in range (1,10) if x%2 == 0} #this gives the cube of even numbers. The cube is generated only when the condition for the even numbers has been satisfied within the specified range
# print(evens_cube)

# #From existing dictionary
# students = {"Ada": 85, "John": 40, "Musa": 65}
# passed_student = {name: score for name, score in students.items() if score >= 50} #defined a dictionary with a key:value pair synonymous to name:score, then assigned the contents of the dictionary called student to name: score provided the coditions have been satified. 
# print(passed_student)

# #Using string keys
# names = ["Ada", "John", "Musa"]
# lengths = {name: len(name) for name in names}
# print(lengths)


# #ACCESSING A DICTIONARY ITEMS
# #Define a dictionary
# student = {"name": "Ada", "age": 20, "course": "Computer Science"}
# #Using key
# print(student["name"])#prints out the value assigned to the key "name"

# #Using get() method to avoid errors if key is missing
# print(student.get("age"))
# print(student.get("grade", "Not Found")) #this specifies the key and what should be printed if error occurs

# #Modifying Dictionaries
# student["age"] = 21 #this changes the value of the key("age") to 21
# student["grade"] = "A" #adds a new key-value pair
# print(student)

# #Removing items from dictionaries
# #Using .pop()
# student.pop("grade") #removes the last key:value pair from the dictionary

# # #Using popitem() 
# # student.popitem() #removes the last inserted key:value pair
# # print(student)

# # #Using del keyword
# # del student["course"] #deletes the value of the specified key

# #Using clear() 
# student.clear() #removes all items from the dictionary


# #DICTIONARY METHODS
# person = {"name": "Emeka", "age": 30}
# #.key()
# print(person.keys()) #prints the keys in the dictionary

# #.values()
# print(person.values()) #prints the values in the dictionary

#.items()
# person.items() #prints out the contents of a dictionary
# print(person)

# #.update()
# person.update({"age": 31, "city": "Lagos"}) #this updates the value of multiple keys at once
# print(person)


# #NESTED DICTIONARies
# students = {
#     "student1": {"name": "Ada", "age": 20}, #The key called student1 has a dictionary as it's value
#     "student2": {"name": "John", "age": 22}
# }
# print(students["student1"]["name"]) #this calls the value of the key name from the key student1


# #LOOPING THROUGH DICTIONARIES
# #Loop through keys
# student = {"name": "Ada", "age": 20, "course": "Computer Science"}
# for k in student:
#     print(k) #prints out the keys from the dictionary on a new line

# #LOOPING THROUGH VALUES
# for val in student.values(): 
#     print(val) #prints the values from the dictionary

# #Looping through key-value pairs
# for key, val in student.items():
#     print(f"{key}: {val}") #prints the key:value pair

# #Storing a student's biodata
# student = {
#     "name": "Chinedu",
#     "age": 19,
#     "department": "Engineering",
#     "subjects": ["Maths", "Physics", "Chemistry"],
#     "is_full_time": True
# }
# print(f"Name: {student['name']}")
# print(f"Subjects: {", ".join(student['subjects'])}")

#Adding key-value pairs to an empty dictionary
student = {}
student["name"] = "Goodness"
student["Interest"] = "AI"
student["Track"] = "AI_Dev"
print(student)

#List of dictionaries. Each student has their own dictionary
students = [
    {"Name": "John", "Interest": "AI", "Track": "AI_Dev"},
    {"Name": "Mary", "Interest": "Cloud Computing", "Track": "AI_Eng"},
    {"Name": "Paul", "Interest": "Cyber Security", "Track": "AI_Dev"}
]
print(students[0]["Name"]) #prints out the value for name from the dictionary with index number 0
print(students[1]["Track"]) #prints out the value for track from the dictionary with index number 1

#Dictionary of dictionaries Each student is keyed by their ID
students = {
  "AI010"   :  {"Name": "John", "Interest": "AI", "Track": "AI_Dev"},
  "AI020" :  {"Name": "Mary", "Interest": "Cloud Computing", "Track": "AI_Eng"},
  "AI030"  :  {"Name": "Paul", "Interest": "Cyber Security", "Track": "AI_Dev"}
}
print(students["AI010"]["Name"]) #the key being the ID number is used to access the value for Name. 
print(students["AI030"]["Track"]) #this prints out AI_Dev for Id AI030

#Dictionary of lists. Each subject stores list of scores
scores = {
    "python":  [5, 78, 92],
    "pandas": [88, 74, 90],
    "Scikit-learn": [80, 95, 87]
}
print(scores["python"]) #prints out a list of scores assigned python
print(scores["pandas"][1]) #prints 74
