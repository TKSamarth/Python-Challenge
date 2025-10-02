# Hypotenuse of the Right Angled Triangle
import math

a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))

hypo = math.sqrt(pow(a, 2) + pow(b, 2))
print("Hypotenuse is: ", round(hypo, 2))