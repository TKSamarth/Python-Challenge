# Temperature Converter

temp = float(input("Enter the temperature value: "))
unit = input("Enter the unit of temperature (C for Celsius, F for Fahrenheit, K for Kelvin): ")

if unit == "C":
    print("Fahrenheit:", (temp * 9/5) + 32)
    print("Kelvin:", temp + 273.15)

elif unit == "F":
    print("Celsius:", (temp - 32) * 5/9)
    print("Kelvin:", ((temp - 32) * 5/9) + 273.15)

elif unit == "K":
    print("Celsius:", temp - 273.15)
    print("Fahrenheit:", ((temp - 273.15) * 9/5) + 32)

else:
    print("Invalid unit! Please enter C, F, or K.")
