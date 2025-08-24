#Task 5 Store inventory update
store = {"Book": 15, "Pen": 20, "Bag": 30}
interest = input(f"The follwing items are available {store}, what would you like to buy: ").title()
quantity = int(input(f"How many {interest}s would you like to buy: "))

store[interest] -= quantity #this subtracts the inputted quantity from the value of the specified interest
print(store) #this prints the latest inventory