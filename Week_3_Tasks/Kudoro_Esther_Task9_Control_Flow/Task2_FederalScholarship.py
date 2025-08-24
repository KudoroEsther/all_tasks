#Federal Government Scholarship Key Eligibility Requirements

name = input("Enter your name: ").title()
subject = ["Maths", "English", "TD", "Chemistry", "Physics"]


citizen = input("Enter your nationality: ").title()

if citizen == "Nigerian":
    enrollment = input("Are you registered full-time undergraduate student of a Nigerian university? Input Yes or No: ").strip().lower()

    if enrollment == "yes":
        scholarship = input("Are you a beneficiary of any other scholarship from an entity in the Oil and Gas industry? Input Yes or No: ").strip().lower()

        if scholarship == "no":
            grade1 = input(f"Input your grade for {subject[0]}, you can only input A or B: ").strip().upper()
            grade2 = input(f"Input your grade for {subject[1]}, you can only input A or B: ").strip().upper()
            grade3 = input(f"Input your grade for {subject[2]}, you can only input A or B: ").strip().upper()
            grade4 = input(f"Input your grade for {subject[3]}, you can only input A or B: ").strip().upper()
            grade5 = input(f"Input your grade for {subject[4]}, you can only input A or B: ").strip().upper()
            grades = grade1, grade2, grade3, grade4, grade5

            if (set(grades)) == {"A", "B"}:
                print(f"Congratulations {name}! You are eligible for this scholarship.")

            else:
                print(f"Unfortunately {name}, you are not eligible for this scholarship")

        else:
            print("You cannot be a current beneficiary of any other scholarship.")

    else:
        print("You must be a registered full-time undergraduate student of a Nigerian university to be eligible for the scholarship.")

else:
    print("You have to be Nigerian to qualify for the scholarship.")