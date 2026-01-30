# Python Functions with Different Parameter Types

# ===== 1. NO PARAMETERS =====
def say_hello():
    """Function with no parameters"""
    print("Hello! Welcome to Python functions!")

# Call the function
say_hello()


# ===== 2. ONE PARAMETER =====
def greet(name):
    """Function with one parameter"""
    print(f"Hi {name}, nice to meet you!")

# Call the function with an argument
greet("Alice")
greet("Bob")


# ===== 3. MULTIPLE PARAMETERS =====
def add(num1, num2):
    """Function with multiple parameters"""
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
    return result

# Call the function with multiple arguments
add(5, 10)
sum_result = add(25, 75)
print(f"The sum is: {sum_result}")


# ===== 4. DEFAULT PARAMETERS =====
def introduce(name, age=20, city="Unknown"):
    """Function with default parameters"""
    print(f"Name: {name}, Age: {age}, City: {city}")

# Call with only required parameter
introduce("John")

# Call with some parameters (overrides defaults)
introduce("Sarah", 25)

# Call with all parameters (overrides defaults)
introduce("Mike", 30, "New York")

# Call with named parameters (keyword arguments)
introduce(name="Emma", city="Boston", age=28)


# ===== BONUS: COMBINING ALL TYPES =====
def create_profile(username, age=18, email="", country="USA"):
    """Function with mixed parameters"""
    profile = {
        "username": username,
        "age": age,
        "email": email,
        "country": country
    }
    return profile

# Different ways to call
profile1 = create_profile("john_doe")
print(profile1)

profile2 = create_profile("jane_smith", 25, "jane@email.com")
print(profile2)

profile3 = create_profile("alex", country="Canada", age=30, email="alex@example.com")
print(profile3)
