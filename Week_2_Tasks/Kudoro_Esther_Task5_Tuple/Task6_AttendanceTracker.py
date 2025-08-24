# Task 6 Attendance tracker
name = input("Enter your namme: ")
gender = input("Enter your gender: ")
course = input("Enter your course track: ")
month_input = int(input("Enter the month number, for example January=1: "))
week_input = int(input("Enter the day number, for example Sunday=1: "))

week = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
month = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
print(type(week))

print(f"Name: {name}")
print(f"Gender: {gender}")

print(f"Month: {month[month_input -1]}") #This is essentially {month[index_number]} where index_number = month_input -1

#This selects the day of the week with an index number that is equal to the inputted number-1. For example, if week_input = 2, the output will be an element with an index number of 2-1, which is Monday in this case.
print(f"Week:  {week[week_input -1]}")