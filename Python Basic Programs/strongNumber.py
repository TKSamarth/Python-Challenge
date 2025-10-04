n = int(input("Enter a number: "))
temp = n
s = 0

while n > 0:
    digit = n % 10
    fact = 1
    for i in range(1, digit + 1):
        fact *= i
    s += fact
    n //= 10

if s == temp:
    print("Strong number")
else:
    print("Not a strong number")
