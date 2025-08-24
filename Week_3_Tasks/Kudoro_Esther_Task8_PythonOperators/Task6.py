#Task 6 Admission Session
#Without Control Flow 

dept = "Computer Engineering"
compulsory = ["Maths", "English", "Physics", "Chemistry"]
cut_off = 230

name = input("Please input your name: ")
print(f"\nWelcome {name} you are registering for admission into the department of {dept} for the 2025/2026 session. \nPlease follow the prompt.")
age =  int(input("\nPlease input your age: "))


utme = int(input("Please input your UTME/JAMB score: "))
choice = input("Did you choose Unilag as your first choice, input Yes or No: ").strip().lower()

print(" ")
print("WAEC RESULT".center(50, "."),"\nYou're to input no grade less than C in the next section!")

sub1 = input(f"\nPlease input your grade for {compulsory[0]}: ").strip().lower()
sub2 = input(f"Please input your grade for {compulsory[1]}: ").strip().lower()
sub3 = input(f"Please input your grade for {compulsory[2]}: ").strip().lower()
sub4 = input(f"Please input your grade for {compulsory[3]}: ").strip().lower()
sub5 = input(f"Please input your grade for the fifth subject: ").strip().lower()
grades = sub1, sub2, sub3, sub4, sub5

Pre_eligibility = (age >= 16) and (utme >= 200) and (choice == "yes") and (set(grades) == {"a", "b", "c"})
print(Pre_eligibility and f"Your POST-UTME is slated for next week.\n" or "You are not eligible to write the POST-UTME")

P_Utme = int(input("Good job on getting this far! \nEnter your POST-UTME score: "))

Post_eligibility = Pre_eligibility and utme >= cut_off and P_Utme >= 60
print(Post_eligibility and f"Congratulations {name}! You have passed all the requirement to be admitted into {dept}. Please check your email for your admission letter \nDo not forget to accept our offer on your JAMB portal." or "Unfortunately, you did not reach cut-off mark to be admitted into the department of {dept}.")