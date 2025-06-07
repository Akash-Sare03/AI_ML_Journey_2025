
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
except ValueError:
    print("Please enter valid integers only.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("Result:", result)
finally:
    print("Program finished.")


## Question 1: File Reader with Error Handling

try:
    filename = input("Enter filename: ")
    with open(filename, 'r') as file:
        content = file.read()
        if not content:
            print("File is empty.")
        else:
            print("File content loaded.")
except FileNotFoundError:
    print("File not found.")
finally:
    print("Operation complete.")


## Question 2: Age Validator using Custom Exception (raise)

try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative!")
    elif age > 120:
        raise ValueError("Age seems unrealistic!")
except ValueError as ve:
    print("Error:", ve)
else:
    print(f"Age is valid: {age}")


## Question 3: Simple Calculator with Error Handling

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    op = input("Enter operation (+, -, *, /): ")

    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        result = num1 / num2
    else:
        raise ValueError("Invalid operation.")
except ValueError as ve:
    print("Error:", ve)
except ZeroDivisionError:
    print("Error: Division by zero.")
else:
    print("Result:", result)
finally:
    print("Calculation attempt complete.")

