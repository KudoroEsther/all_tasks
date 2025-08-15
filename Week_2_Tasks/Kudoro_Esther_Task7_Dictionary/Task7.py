#Task 1 Student biodata storage
info = {
    "Name": input("Input your name: "),
    "age": int(input("Enter your age: ")),
    "gender": input("Input your gender: "),
    "course": input("Enter your course: ").split()
}
# print(*info.items(), sep="\n")
for key, val in info.items():
    print(f"{key}:\t{val}") #prints the content of the dictionary on a new line with tab in between

# #Task 2 Super market price list
# # items_price = {}
# item = ["rice", "beans", "banana", "mango"]
# i=0
# prices = []
# # prices = input(f"Enter the price for each item: ")
# for i in item:
#     price = int(input(f"Enter the price for {i}: "))
#     prices.append(price)
#     # items_price[f"{item}"] = price
# items_price = zip(item,prices)
#     # itemss = {item:prices}
# print(items_price)
# print(prices)
# print(f"{item}:{prices}")

# items_price = {item, price}
# print(items_price)


#create a list with items
#creat a variable that accepts integer inputs for the price
#add list and price to a dict known as list_price

# item = ["rice", "beans", "banana", "mango"]

# price = int(input(f"Enter the price for {item}"))