# Task 5 Contact quick lookup
name = ("Esther", "May", "Konrad")
phone = (909, 902, 903)
name_phone = dict(zip(name,phone))
print(name_phone)

ask_name = input("Input a name to view their phone number: ").title()

ask_name in name #this checks if the inputted name exists
print(name_phone.get(ask_name, "Name not found, try again")) #.get() is used to display the value of the name input otherwise an error message

