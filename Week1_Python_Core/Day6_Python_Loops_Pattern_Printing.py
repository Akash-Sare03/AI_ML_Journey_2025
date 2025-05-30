 ## Problem 1: Print Floyd’s Triangle

n = int(input("Enter Number of rows: "))
print("Floyd’s Triangle")


count = 1

for i in range(1, n + 1):
    for j in range(i):
        print(count,end=" ")
        count += 1
    print()
    





## Problem 2: Inverted Pyramid of Stars

n = int(input("Enter number of rows: "))


for i in range(n):
    space = " " * i
    stars = "*" * (2*(n-i) - 1)
    print(space + stars)







# Problem 3: Diamond Pattern of Stars

n = int(input("Enter number of rows: "))

# Top half
for i in range(1, n + 1):
    spaces = " " * (n - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)

# Bottom half
for i in range(n - 1, 0, -1):
    spaces = " " * (n - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)


# Problem 4: Hollow Right-Angled Triangle

n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j == 1 or j == i or i == n:
            print("*", end="")
        else:
            print(" ", end="")
    print()






# Problem 5: Pascal’s Triangle

n = int(input("Enter number of rows: "))

for i in range(n):
    # Print spaces for alignment
    for j in range(n - i - 1):
        print(" ", end="")

    # Initialize first value of row as 1
    num = 1
    for j in range(i + 1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)  # Compute next value

    print()  # Move to next line
