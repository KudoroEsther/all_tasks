seat = set(i for i in range (1,51))
# print(seat)
booked = []
names = {}



for r in range (1,51):
    name = input("\nEnter your name: ").strip().title()
    if name not in names: #this ensures that multiple seats aren't booked by a single individual
        names[name] = None #set the inputted name a key and the value as None
        book = int(input(f"Seat numbers {seat} are available, input a seat number to book a seat: ")) #accepts seat number from user

        if book in booked: #checks if the inputted seat number has been booked or not
            print(f"Seat {book} has been booked. Try again")

        elif book > 50: #accounts for stubborn users
            print("Invalid seat number")
            break

        else:
            seat_left = seat.discard(book) #removes the unique seat number inputted by the user from the set
            booked.append(book) #add the seat number to the list booked
            namees = {}
            namees[name]= book
            names[name] = book #assigns the seat number as a value to their name w
            print(f"Your booking details is as follows name: seat_number \n{namees}")

    else:
        print("You cannot book multiple seats.")
        break

#run as long as seat is not empty, when seat is empty, print all seats are booked
#accept name, and seat number if seat number is booked print an error and restart the progream
#ask user if they want to register another seat, if yes restart the program, else end the program?
#what if they want to book multiple seats at a time?