# #TASK 8
# #Task 3 Online store cart calculation
# items = ["Book", "Pen", "Bag", "Water"]
# price = [500, 100, 1000, 50]

# cart_total = 0

# cart_total += price[0]
# cart_total += price[1]
# cart_total += price[2]
# cart_total += price[3]
# print(f"Items: {items} \nTotal Price: ₦{cart_total}")

# #Task 4 Student Record
# student = {}
# name = input("Please enter your name: ").strip().title()
# age = int(input("Please enter your age: "))

# student["Name"] = name
# student["Age"]= age

# scores =  [70, 85, 90, 100]
# student["Scores"]= scores

# if min(scores) >= 50:
#     student["Passed"] = True

# else:
#     student["Passed"] = False

# if age >= 13 or age <= 19:
#     student["Teenager"] = "Teenager"
# else: 
#     student["Teenager"] = "Not a teenager"

# for key, value in student.items():
#     print(f"{key}: {value}")

# #Task 5 Store Inventory Update
# store = {"Book": 12, "Pen": 20, "Bag": 18, "Water": 17}
# item = input("Please enter the item you would like to buy: ").title()

# if item in store:
#     quantity = int(input(f"How many {item}s would you like to buy: "))
    
#     if quantity > store[item]:
#         print(f"{quantity} is more than the store's inventory")

#     else: 
#         print(f"Before purchase: {store}")
#         store[item] -= quantity
#         print(f"After purchase: {store}")

# else:
#     print(f"{item} not in store.")
    

#TASK 7
#Task 1 Student biodata storage
total_bio = {}

while True: 
    bio = {}

    name = input("\nPlease enter your name: ").strip().title()
    age = int(input("Please enter your age: "))
    gender = input("Please enter your gender: ").strip().title()
    courses = ["Math", "English", "Geography", "Biology", "Economics"]

    # bio["Name"] = name
    bio["Age"] = age
    bio["Gender"] = gender
    bio["Course"] = courses

    total_bio[name] = bio

    ends = input("Type end to exit the program: ").strip().lower()
    if ends == "end":
        print("Ending the program...")
        break
    else:
        continue
print(total_bio)
# bio.update({'Name': name})

# #Super market price list
# items = ["Sneakers", "Mars", "Water"]
# prices = []

# for i in items:
#     price = int(input(f"Enter the price for {i}: "))
#     prices.append(price)

# print("ITEM \t PRICE")
# for x , y in zip(items, prices):
#     print(f"{x}: {y}")
# print(prices)
