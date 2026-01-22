def add(x, y):
    """Add two numbers"""
    return x + y


def subtract(x, y):
    """Subtract two numbers"""
    return x - y


def multiply(x, y):
    """Multiply two numbers"""
    return x * y


def divide(x, y):
    """Divide two numbers"""
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y


def main():
    """Main calculator function"""
    print("=== Simple Calculator ===")
    
    while True:
        try:
            print("\nOperations:")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            print()

            # Get input from user
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            print("\nChoose operation:")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            choice = input("Enter operation (1/2/3/4): ")

            # Perform calculation based on choice
            if choice == "1":
                print(f"\n{num1} + {num2} = {add(num1, num2)}")
            elif choice == "2":
                print(f"\n{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == "3":
                print(f"\n{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == "4":
                try:
                    print(f"\n{num1} / {num2} = {divide(num1, num2)}")
                except ValueError as e:
                    print(f"\nError: {e}")
            else:
                print("\nInvalid operation choice. Please select 1, 2, 3, or 4.")

        except ValueError as e:
            print(f"\nError: Please enter valid numbers. {e}")
        
        # Ask if user wants to continue
        again = input("\nDo you want to perform another calculation? (yes/no): ").lower()
        if again not in ["yes", "y"]:
            print("\nThank you for using the calculator!")
            break


if __name__ == "__main__":
    main()
