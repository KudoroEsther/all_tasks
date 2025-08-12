#Task 6 Electricity Bill Formatter
name = input("Please input your full name: ")
UnitConsumed = int(input("Please input the number of units consumed in kWh: "))
cost = float(input("Include the cost of electricity per unit: "))
bill = float(cost*UnitConsumed )
print(f"Hello {name} \n\t\tYour light bill is as follows \nUnits consumed in kWh:\t{UnitConsumed} \
\tCost per unit:\t{cost} \nYour total bill is: ₦{bill}kobo")
