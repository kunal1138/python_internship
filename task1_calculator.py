# Task 1: Simple Calculator

print("Simple Calculator")
print("Operations: +, -, *, /")

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Choose an operation (+, -, *, /): ").strip()

    if operation == "+":
        print("Result:", num1 + num2)

    elif operation == "-":
        print("Result:", num1 - num2)

    elif operation == "*":
        print("Result:", num1 * num2)

    elif operation == "/":
        if num2 == 0:
            print("Error: Cannot divide by zero.")
        else:
            print("Result:", num1 / num2)

    else:
        print("Invalid operation. Choose +, -, *, or /.")

except ValueError:
    print("Invalid input. Please enter numbers only.")