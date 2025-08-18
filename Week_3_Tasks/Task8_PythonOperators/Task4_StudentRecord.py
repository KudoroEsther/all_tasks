#Task 4 Student Record
student = {}
name = input("Enter your name: ")
age = int(input("Enter your age: "))
student.update({"Name": name, "Age": age})

scores = [78, 79, 89, 99]
student.update({"Score": scores})

average_score = sum(scores)/len(scores)
passed = average_score >= 50
student.update({"Passed": passed})

teenager = (age >= 13) and (age <= 19)
print(f"Student Record: \nName: {student["Name"]} \nAge: {student["Age"]} \nPassed: {student["Passed"]} \nTeenager: {teenager}")

