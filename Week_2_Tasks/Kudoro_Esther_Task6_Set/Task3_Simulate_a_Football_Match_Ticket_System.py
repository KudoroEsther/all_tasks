#Task 3 Simulate a football match ticket system
seats = set(i for i in range (1,51)) #this stores the seats numbers 1- 50 in a set

book = int(input(f"There are {len(seats)} seats avaialable, pick a number to book a seat: ")) #displays the number of available seats and accepts booking
seats_left = seats.discard(book) #removes the booked seat from the set
print(f"You have reserverd seat {book}")
print(len(seats)) #prints the number of seats remaining
