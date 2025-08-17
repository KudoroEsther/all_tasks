#Task 4 Unique members registration
dict_name ={}
name = input("Enter three names separated by commas: ").title().split(",")
set_name = set(name) #this converts the inputted names to as set

dict_name[f"{name[0]}"]= len(name[0]) #this fills in the empty dictionary, where, the key is the name with index number 0 and the value is the length of the name
dict_name[f"{name[1]}"]= len(name[1])
dict_name[f"{name[2]}"]= len(name[2])

print(dict_name) 
