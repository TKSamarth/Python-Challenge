num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
op = input("Enter an operator (+, -, *, /, %): ")

if op == "+":
    print("Addition:", num1 + num2)

elif op == "-":
    print("Subtraction:", num1 - num2)

elif op == "*":
    print("Multiplication:", num1 * num2)

elif op == "/":
    if num2 != 0:
        print("Division:", num1 / num2)
    else:
        print("Error: Division by zero is not allowed.")

elif op == "%":
    if num2 != 0:
        print("Remainder:", num1 % num2)
    else:
        print("Error: Division by zero is not allowed.")

else:
    print("Invalid operator! Please enter one of +, -, *, /, %.")
