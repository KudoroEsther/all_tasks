#Task 11 Nigerian Currency Converter 
amount = float(input("Please input the amount to be converted in naira: "))
dollars = float(input("Please input the exchange rate from naira to US Dollars: "))
pounds = float(input("Please input the exchange rate from naira to British pounds: "))
ConvertedDollars = float(amount*dollars)
ConvertedPounds = float(amount*pounds)
print(f"Amount in naira(₦) \tAmount in US Dollars($) \tAmount in British Pounds(£) \n{amount:,} \t\t{ConvertedDollars:,} \t\t\t{ConvertedPounds:,}")