
#get user's details like name, age, gender
#use nested if starting with age then utme score
#accepts subjects check that grades aren't less than Cs
#print out that they're eligible for postutme

#set departmental cut-off mark as 230
#offer admission to students who met the departmental cut-off mark and have a post utme score greater than 60
#account for invalid scores


dept = "Computer Engineering"
compulsory = ["Maths", "English", "Physics", "Chemistry"]
cut_off = 230

name = input("Please input your name: ")
print(f"\nWelcome {name} you are registering for admission into the department of {dept} for the 2025/2026 session. \nPlease follow the prompt.")
age =  int(input("\nPlease input your age: "))



#starting with nested if
if age >= 16:
    utme = int(input("Please input your UTME/JAMB score: "))
    choice = input("Did you choose Unilag as your first choice, input Yes or No: ").strip().lower()

    if utme >= 200 and choice == "yes" and utme <= 400:
        print(" ")
        print("WAEC RESULT".center(50, "."),"\nYou're to input no grade less than C in the next section!")

        sub1 = input(f"\nPlease input your grade for {compulsory[0]}: ").strip().lower()
        sub2 = input(f"Please input your grade for {compulsory[1]}: ").strip().lower()
        sub3 = input(f"Please input your grade for {compulsory[2]}: ").strip().lower()
        sub4 = input(f"Please input your grade for {compulsory[3]}: ").strip().lower()
        sub5 = input(f"Please input your grade for the fifth subject: ").strip().lower()

        grades = sub1, sub2, sub3, sub4, sub5
        if set(grades) == {"a","b","c"}:
            print("Your POST-UTME is slated for next week.\n")
            P_Utme = int(input("Good job on getting this far! \nPlease input your POST-UTME score: "))
            if utme >= cut_off and P_Utme >= 60 and P_Utme <=100:
                print(f"Congratulations {name}! You have passed all the requirement to be admitted into {dept}. Please check your email for your admission letter \nDo not forget to accept our offer on your JAMB portal.")
            else:
                print(f"Unfortunately, you did not reach cut-off mark to be admitted into the department of {dept}.")
        else:
            print("You're not eligible to write the POST-UTME as your grades are not up to the requirements.")
    else:
        print("Your UTME score is invalid, therefore you cannot be considered for admission.")
else:
     print(f"You are to young to undergo the admission process, reapply in {16-age} years.")

#get user's details like name, age, gender
#use nested if starting with age then utme score
#accepts subjects check that grades aren't less than Cs
#print out that they're eligible for postutme

#set departmental cut-off mark as 230
#offer admission to students who met the departmental cut-off mark and have a post utme score greater than 60
#account for invalid scores