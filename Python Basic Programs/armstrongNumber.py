n = int(input("Enter a number: "))
temp = n
digits = 0
t = n

while t > 0:
    digits += 1
    t //= 10

s = 0
t = n
while t > 0:
    digit = t % 10
    s += digit ** digits
    t //= 10

if s == temp:
    print("Armstrong number")
else:
    print("Not Armstrong")
