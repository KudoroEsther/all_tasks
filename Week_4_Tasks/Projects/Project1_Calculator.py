#Simple Calculator program

#Defining the functions
#Addition
def add(num1, num2):
    """Adds two numbers supplied by the user"""
    return num1 + num2

def subtract(num1, num2):
    """Subtracts two numbers supplied by the user"""
    return num1 - num2

def multiply(num1, num2):
    """Mulitiplies two numbers supplied by the user"""
    return num1 * num2

def divide(num1, num2):
    """Divides a number by another number supplied by the user"""
    if num2 !=0:
        return num1 / num2
    else:
        return "Error: zero cannot be used as a divisor."
    
def square_root(num1):
    """Gives the square root of a number inputted by the user"""
    return num1 ** 0.5 #raises the inputted number to the power of 1/2

def exponent(num1, num2):
    """Gives the exponent of a number"""
    return num1 ** num2

while True:
    #Displaying options
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square root")
    print("6. Exponent")
    print("0. Exit")

    #Accepting inputs from the user
    choice = input("Enter an option between 1 and 6 or 0 to exit the calculator: ")

    try:
        if choice == "0":
            print("Ending the program...") #break should be used here
            break

        elif choice == "1": #Addition
            print("\nAddition")
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
            print(f"The addition of {num1} and {num2} is {add(num1, num2)}")

        elif choice == "2": #Subtraction
            print("\nSubtraction")
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
            print(f"{num1} - {num2} is {subtract(num1, num2)}")

        elif choice == "3": #Multiplication
            print("\nMultiplicaiton")
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
            print(f"The multiplication of {num1} and {num2} is {multiply(num1, num2)}")

        elif choice == "4": #Division
            print("\nDivision")
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
            print(f"The division of {num1} and {num2} is {divide(num1, num2)}")

        elif choice == "5": #Square root
            print("\nSquare root")
            num1 = float(input("Enter your number: "))
            print(f"The square root of {num1} is {square_root(num1)}")

        elif choice == "6":
            print("\nExponent")
            num1 = float(input("Enter the base number: "))
            num2 = float(input("Enter the power: "))
            print(f"{num1} raised to power {num2} is {exponent(num1, num2)}")
        else:
            pass
    except Exception:
        print("Invalid input, try again")