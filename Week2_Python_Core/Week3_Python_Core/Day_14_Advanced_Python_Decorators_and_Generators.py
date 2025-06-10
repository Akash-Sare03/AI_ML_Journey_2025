
## Decorator : Logging Function Calls with Arguments

def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_call
def greet(name):
    print(f"Hello, {name}!")

greet("Akash")



## Generators in Python

def generate_numbers(n):
    for i in range(n):
        yield i

gen = generate_numbers(5)

for num in gen:
    print(num)


## Even Number Generator

def generate_even(n):
    for i in range(n + 1):     # include 'n' itself
        if i % 2 == 0:
            yield i            # yield only even numbers

even = generate_even(10)

for i in even:
    print(i)
