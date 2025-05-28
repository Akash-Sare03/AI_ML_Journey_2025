
## 1. Write a function called greet_user that takes a user's name as input and prints a greeting message.

def greet_user(name):
    print("hello",name,"! Welcome back.")

user_name = input("Enter your name: ")

greet_user(user_name)


## 2. Write a function called check_even_odd that takes a number as input and returns whether it’s even or odd.

def check_even_odd(a):
    if a%2==0:
        print("Even")
    else:
        print("Odd")
check_even_odd_=int(input("Enter a number: "))

check_even_odd(check_even_odd_)


## 3. Multiply All Numbers Using *args

def multiply_all(*args):      # Step 1: accept multiple values
    result = 1                # Step 2: start with 1 (not 0 — multiplication identity)
    for num in args:          # Step 3: go through each number
        result *= num         # Step 4: multiply one by one
    return result             # Step 5: return the final result

# Taking comma-separated values from user

nums = input("Enter numbers separated by comma: ")
num_list = [int(i) for i in nums.split(",")]

# Passing the list using * unpacking
print("Multiplication result:", multiply_all(*num_list))
