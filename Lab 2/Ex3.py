# Ask the user to enter a flaoting point number, Square the number.
#Print out the original number and the squared result.
#Name : Beverly Mambou
#Date : 1/22/2026

input_value = input("Please enter a floating point number: ")
float_value = float(input_value)
squared_value = float_value ** 2

#Round the number to 2 decimal places
squared_value = round(squared_value, 2)

print("You entered:", float_value)
print(f"The square of {float_value} is {squared_value}")
