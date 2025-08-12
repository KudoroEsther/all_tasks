#Task 5 Daily Market Report
market = input("Please input the name of the market: ")
traders = int(input("Please input the number of traders in the market: "))
revenue = float(input("Please input the total revenue generated in the market: "))
#using comma for thousands separator
print(f"The name of the market is {market}, there are {traders} traders, the total revenue generated is ₦{revenue:,}kobo.")
