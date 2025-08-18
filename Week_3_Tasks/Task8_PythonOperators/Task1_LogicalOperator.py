#Task 1
"""
Explaining the output of the program print("{num1} == {num2} : {num1 == num2}")
Assuming num1 = 5 num2 = 6
Output = False

The first part {num1} == {num2} : prints out the inputs to num1 and num2 with the symbols ==
{num2} : {num1 == num2} This checks if the inputted number in num1 is equal to the inputted number in num2. Since the numbers in num1 and num2 are not equal the output will be False"""

"""Explaining the output of the program print(f"{num1} != {num2} : {num1 != num2}")
Assuming num1 = 5 num2 = 6
Output = True

{num1 != num2} This checks that the content of num1 is not equal to that of num2 and prints out True
"""

"""
Explaining the output of the program print(f"{num1} > {num2} : {num1 > num2}")
Assuming num1 = 5 num2 = 6
Output = False

{num1 > num2} this checks if the content of num1 is greater than the content of num2. Since 5 is not greater than 6, our output is False
"""

"""
Explaining the output of the program print(f"{num1} < {num2} : {num1 < num2}")
Assuming num1 = 5 num2 = 6
Output = True

{num1 < num2} this checks if the content of num1 is less than the content of num2. Since 5 is less than 6, our output is True.
"""

#Use cases
#Account number registration
"""
The program given can be used in ensuring the uniqueness of account numbers during account registration. Num1 could be the account number of customer 1 while num2 could be the account number for customer 2. The logic operator (==) can be used to confirm that both customers do not have the same account numbers.
"""
#Change of passcode for a phone
"""
The logic operators (== or !=) can be used to verify if the passcode input in num1 is the same as the passcode given in num2. If they're the same, the inputted passcode is registered, otherwise, the user is prompted to try again.
"""
#Inventory verification
"""
The program given can be used to verify that the inventory records inputted by two warehous staff are the same using logic operators such as (==, !=, >, <)
"""

#Change of passcode
num1 = int(input("Enter your new passcode: "))
num2 = int(input("Confirm your new passcode: "))
if num1 == num2:
    print(f"Your passcode {num2} has been registered")
print("Try again")