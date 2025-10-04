base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))
result = 1
count = 0

while count < exp:
    result *= base
    count += 1

print("Result:", result)
