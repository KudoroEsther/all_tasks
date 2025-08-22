seat = set(i for i in range (1,51))
# print(seat)

name = input("Enter your name: ").strip()

book = int(input(f"There are {len(seat)} seats left, input a seat number to book a seat: "))
seat_left = seat.discard(book)
print(seat)

#run as long as seat is not empty, when seat is empty, print all seats are booked
#accept name, and seat number if seat number is booked print an error and restart the progream
#ask user if they want to register another seat, if yes restart the program, else end the program
#what if they want to book multiple seats at a time