#Error Handling
seat = set(i for i in range (1,51))
booked = [] #this stores the booked seats
total_names = {} #this stores the information of all booked seats with the corresponding user's name


for r in range (1,51):
    name = input("\nEnter your name full name: ").strip().title()
    total_names[name] = None #set the inputted name a key and the value as None

    try: 
            book = int(input(f"Seat numbers {seat} are available, input a seat number to book a seat: ")) #accepts seat number from user

            if book in booked: #checks if the inputted seat number has been booked or not
                print(f"Seat {book} has been booked. Try again")

            elif book > 50: #accounts for stubborn users
                print("Invalid seat number")
                # break

            else:
                seat_left = seat.discard(book) #removes the unique seat number inputted by the user from the set
                booked.append(book) #add the seat number to the list booked
                individual_names = {} #this stores the booking information of the current user
                individual_names[name]= book
                total_names[name] = book #assigns the seat number as a value to their name w
                print(f"Your booking details is as follows name: seat_number \n{individual_names}")
                print(total_names)

    except ValueError:
        print("Invalid input, your input must be an integer.")
    
    

#run as long as seat is not empty, when seat is empty, print all seats are booked
#accept name, and seat number if seat number is booked print an error and restart the progream
#ask user if they want to register another seat, if yes restart the program, else end the program?
#what if they want to book multiple seats at a time?