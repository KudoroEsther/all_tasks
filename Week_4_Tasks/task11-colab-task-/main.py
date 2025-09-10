from pathlib import Path
from participant_pkg import file_ops
# import file_ops
workspace = Path("workspace")
workspace.mkdir(exist_ok=True)
path = workspace / "contacts.csv"
participant_dict = {}

while True:
    while True:
        try:
            name = input("Enter your name: ").title()
            if name == "":
                print("Name cannot be blank.")
                continue
            elif name.isdigit():
                print("Name cannot be a digit.")
                continue
            else:
                print(f"Name is: {name}")
                participant_dict["name"] = name
                break
                
        except Exception as e:
            print(f"The error was {e}")
            
    while True: 
        try:
            age = input("Enter your age: ")
            if age == "":
                print("This field (age) cannot be left blank")
                continue
            
            else:
                print(f"Age: {age}")
                age = int(age)
                participant_dict["Age"] = age
                break
        except ValueError as e:
            print("Age should be a whole number")
        # except Exception as e:
        #     print(f"{e}")
            
    while True:
        try:
            phone_number = input("Enter your phone number: ")
            if phone_number == "":
                print("This field(phone_number) cannot be left empty")
            elif phone_number.isalpha():
                print("Phone number must be a digit.")
            elif len(phone_number) != 11:
                print("Wrong length for phone number. The entry must be exactly 11 digits.")
                continue
                
            else:
                print(f"Phone number: {phone_number}")
                participant_dict["Phone_number"] = phone_number
                break
        except Exception as e:
            print(f"The error was {e}")
    while True:            
        try:
            track = input("Enter your track: ")
            if track == "":
                print("This field (track) cannot be left blank")
                continue
            elif track.isdigit():
                continue
            else:
                print(f"Track: {track}")
                participant_dict["Track"] = track
                break
            
        except Exception as e:
            print(f"The error was {e}")
                
    file_ops.save_participant(path, participant_dict)
    exit = input("Input \"done\" if you are done with your entries").title()
                
    if exit == "Done":
        break



    # file_ops.save_participant(path, participant_dict)

file_ops.load_participants(path)
