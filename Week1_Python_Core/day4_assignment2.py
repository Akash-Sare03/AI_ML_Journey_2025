
## 2. Factorial using Recursion

def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a non-negative integer: "))
result = factorial(num)
print(f"Factorial of {num} is {result}")

## Factorial using iterative

def factorial_iterative(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

num = int(input("Enter a non-negative integer: "))
print(f"Factorial of {num} is {factorial_iterative(num)}")



