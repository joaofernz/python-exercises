import math


def addition():
    print("Addition")
    n = float(input("Enter the first number: "))
    m = float(input("Enter the second number: "))
    return n + m


def subtraction():
    print("Subtraction")
    n = float(input("Enter the first number: "))
    m = float(input("Enter the second number: "))
    return n - m


def multiplication():
    print("Multiplication")
    n = float(input("Enter the first number: "))
    m = float(input("Enter the second number: "))
    return n * m


def division():
    print("Division")
    n = float(input("Enter the first number: "))
    m = float(input("Enter the second number: "))
    if m != 0:
        return n / m
    else:
        return "Error: Cannot divide by zero"


def square():
    print("Square")
    n = float(input("Enter the number: "))
    return n ** 2


def square_root():
    print("Square Root")
    n = float(input("Enter the number: "))
    if n >= 0:
        return math.sqrt(n)
    else:
        return "Error: Cannot calculate square root of a negative number"


def calculator():
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square")
    print("6. Square Root")

    choice = input("Enter choice (1/2/3/4/5/6): ")

    if choice == '1':
        print("Result:", addition())
    elif choice == '2':
        print("Result:", subtraction())
    elif choice == '3':
        print("Result:", multiplication())
    elif choice == '4':
        print("Result:", division())
    elif choice == '5':
        print("Result:", square())
    elif choice == '6':
        print("Result:", square_root())
    else:
        print("Invalid input")


# Call the calculator function to start the calculator
calculator()
