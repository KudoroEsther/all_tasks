#Task 3 Days and acitvities pairing
week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
activity = [] #created an empty list in order to use 

for i in week[::3]: #this picks three days from the tuple using a steps size of three
    act = input(f"Enter the activity for {i}: ").split() #accepts input for the days picked using the for loop
    activity.append(act) #this adds the inputted activity to a list

zipped = {week:activity for week,activity in zip(week[::3],activity)} #zip is used to combine week and activity, just like a zipper does
print(zipped)

#OR
#this is more straightforward.
act1 = input(f"Input an activity for {week[0]}: ")
act2 = input(f"Input an activity for {week[1]}: ")
act3 = input(f"Input an activity for {week[2]}: ")
acts = act1, act2, act3 #assigns to the contents of multiple variables to a single variable
days_pairing = dict(zip(week,acts))
print(days_pairing)

