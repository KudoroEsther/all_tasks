#Welcome greeting
#ask for ussd code, store in a variable
#wile true for menu, an option to exit
#if for each option

"""
THE LOGICAL PROCESS
accepted ussd from user, used strip to mitigate user error
checks if the user USSD input is right
used while True to ensure that the programs runs as long as the specified conditions are satisfied, otherwise, it prints an error message and restarts the loop

Accepts input from user regarding their desired service (for example, check balance...)
check if the user's input aligns with any of the predefined premises, for example, an input of  1 = should check data and airtime balance. Else it prints an error message and restarts the loop
If the user's input aligns with the required condition it prints out the appropriate messages, and breaks the program
"""

data = 10343.67
airtime = 1000.87

print("Welcome to MTN".center(50, " "))
try:
    code = input("\nEnter USSD '*312#': ").strip()
    if code == "*312#":
        while True:
            option = int(input("\nChoose an option \n1. Check Data and Airtime Balance \n2. Buy Airtime \n3. Buy Data \n4. Exit \n-> "))

            #if the user chooses to check their balance
            if option == 1:
                print(f"Your data balance is {data}MB \nYour airtime balance is ₦{airtime}kobo")
                break

            #if the user chooses to buy airtime
            elif option == 2:
                buy_air = int(input("How much airtime would you like to buy? Enter digits only-> "))
                airtime += buy_air
                print(f"Your airtime balance is ₦{airtime}kobo")
                break #using break to ensure the program does not restart after the section above has been executed
            

            #if the user chooses to buy dataa
            elif option == 3:
                buy_data = int(input("\nBuy Data plans \n1. Weekly \n2. Monthly \n-> "))

                #if the user chooses to buy weekly data
                if buy_data == 1:
                    weekly = int(input("\n1. ₦75 for 75MB \n2. ₦110 for 110MB \n3. ₦1000 for 1GB\n-> "))

                    if weekly == 1:
                        if 75 > airtime: #this part accounts for insufficient balance
                            print("Insufficient airtime balance.")
                        else:
                            data += 75
                            airtime -= 75
                            print(f"You bought 75MB weekly data, your data balance is {data}MB \nAirtime balance is ₦{airtime}kobo")
                            break

                    elif weekly == 2:
                        if 100 > airtime: #this part accounts for insufficient balance
                            print("Insufficient airtime balance.")
                        else:
                            data += 110
                            airtime -= 100
                            print(f"You bought 110MB weekly data, your data balance is {data}MB \nAirtime balance is ₦{airtime}kobo")
                            break

                    elif weekly == 3:
                        if 1000 > airtime: #this part accounts for insufficient balance
                            print("Insufficient airtime balance.")
                        else:
                            data += 1024
                            airtime -= 1000
                            print(f"You bought 1GB weekly data, your data balance is {data}MB \nNew airtime balance is ₦{airtime}kobo")
                            break
                    else: #if the user chooses none of the options in weekly data
                        print("Invalid input, try agian.")


                #If the user chooses to buy monthly data
                elif buy_data == 2:
                    monthly = int(input("\n1. ₦1,500 for 1.8GB \n2. ₦2,000 for 2.7GB \n3. ₦3,500 for 7GB \n-> "))

                    #For 1.8GB monthly data
                    if monthly == 1:
                        if 1500 > airtime: #this part accounts for insufficient balance
                            print("Insufficient airtime balance.")
                        else:
                            data += 1843.2
                            airtime -= 1500
                            print(f"You bought 1.8GB monthly data, your data balance is {data}MB \nNew airtime balance is ₦{airtime}kobo")
                            break

                    #For 2.7GB monthly data
                    elif monthly == 2:
                        if 2000 > airtime:
                            print("Insufficient airtime balance.")
                        else:
                            data += 2764.8
                            airtime -= 2000
                            print(f"You bought 2.7GB monthly data, your data balance is {data}MB \nNew airtime balance is ₦{airtime}kobo")
                            break

                    #For 7GB monthly data
                    elif monthly == 3: 
                        if 3500 > airtime:
                            print("Insufficient airtime balance.")
                        else:
                            data += 7168
                            airtime -= 3500
                            print(f"You bought 7GB monthly data, your data balance is {data}MB \nNew airtime balance is ₦{airtime}kobo")
                            break
                    else: #if the user chooses none of the options available in monthly data
                        print("Invalid input, try agian.")
                
                else: #if the user chooses neither weekly nor monthly data
                        print("Invalid input, try agian.")

            #if the user chooses to exit the program
            elif option == 4:
                print("Exiting the program...")
                break
            else: #if the user chooses an option that isn't available
                print("Invalid input, try agian.")
    else:
        print("Invald input, try again.")
except ValueError as v:
    print("Error", v)
except Exception as e:
    print("Error", e)
except TypeError as t:
    print("Error", t)
finally:
    print("Transaction Stopped.")