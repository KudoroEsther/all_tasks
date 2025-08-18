# Task 3 Online store cart calculation
items = ["Laptop", "Book", "Phone"]
prices = [5000, 100, 2000]
cart_total = 0

cart_total += prices[0] #this adds the first element in prices to cart_total
cart_total += prices[1]
cart_total += prices[2]
print(cart_total)

print(f"Items: {items} \nTotal Price: ₦{cart_total:,}") #:, is a thousand separator, it separates thousands