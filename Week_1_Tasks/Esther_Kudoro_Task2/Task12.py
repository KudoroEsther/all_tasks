#Task 12 Simulated USSD Menu Interaction
print("Welcome to MTN Customer Service!")
ussd = input("Dial *310#: ")
print("1) Check Balance \n2) Buy Airtime \n3) Buy Data")
choice = input("Choose either option 1, 2, or 3: ")
data = float(20989.23)
airtime = float(200.5)
print(f"You chose option {choice} your data balance is {data}.")
print(f"Thank you for choosing MTN your airtime balance is {airtime} \
to buy data, repeat the transaction and pick option 3. Thank you!")