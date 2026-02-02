import HandyMath 

#Ask the user for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

#Use functions from HandyMath 
mid = HandyMath.midpoint(num1, num2)
sqrt1 = HandyMath.squareroot(num1)
power = HandyMath.exponent(num1, num2)
maximum = HandyMath.max(num1, num2)
minimum = HandyMath.min(num1, num2)

#print results using f-strings
print(f"The midpoint between {num1} and {num2} is: {mid}")
print(f"The square root of {num1} is: {sqrt1}")
print(f"{num1} raised to the power of {num2} is: {power}")
print(f"The maximum of {num1} and {num2} is: {maximum}")
print(f"The minimum of {num1} and {num2} is: {minimum}")

from HandyMath import max, min

