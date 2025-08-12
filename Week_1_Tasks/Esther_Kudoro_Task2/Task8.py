#Task 8 Transport Fare Calculator
distance = float(input("Please input the distance in km: "))
fare = float(input("Please input the fare per km: "))
TotalFare = float(distance*fare)
print(f"Your total fare for {distance}km is {TotalFare:.2f}")
