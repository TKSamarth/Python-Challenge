# Weight Converter

weight = float(input("Enter your weight: "))
unit = input("Enter the unit (kg/lbs): ")

if unit == "kg":
    converted = weight * 2.205
    print(f"Your weight after converting is: {round(converted, 2)} lbs")

elif unit == "lbs":
    converted = weight / 2.205
    print(f"Your weight after converting is: {round(converted, 2)} kg")

else:
    print("Invalid Unit! Please enter 'Kg' or 'lbs'.")
