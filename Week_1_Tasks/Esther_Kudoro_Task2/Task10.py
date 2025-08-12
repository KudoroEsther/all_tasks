#Task 10 School Fees Breakdown
name = input("Please input the name of the school: ")
tution = float(input("Please input the tution fee: "))
HostelFee = float(input("Please input the hostel fee: "))
FeedingFee = float(input("Please input the feeding fee: "))
total = float(tution*HostelFee*FeedingFee)
print(f"\t\t\tFees breakdown for {name} \nTution fee: {tution} \nHostel Fee: {HostelFee}\
\nFeeding fee: {FeedingFee} \nTotal: ₦{str(total)}kobo")
