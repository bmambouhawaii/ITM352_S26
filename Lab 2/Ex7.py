# Ask the user to ebter a temperature in Farenheit.
# Convert the temperature to Celsius (C = (F - 32) * 5/9).
# Name : Beverly Mambou
# Date : 1/22/2026  

farenheit_input = input("Please enter a temperature in Farenheit: ")
farenheit_value = float(farenheit_input)
celsius_temp = (farenheit_value - 32) * 5 / 9
celsius_temp_rounded = round(celsius_temp, 1)
print("You entered:", farenheit_value)
print(f"The temperature in Celsius is: {celsius_temp_rounded} °C")

