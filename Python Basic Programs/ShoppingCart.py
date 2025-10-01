item = input("What item would you like to buy?: ")
price = float(input("What is the cost?: "))
quantity = int(input("How many would you like to buy?: "))

total = price * quantity

print(f"You just bought {quantity} {item}/s")
print(f"Your total is {total}")
