
## Q3: Find the maximum value in a list without using the max() function.

def find_max_value(numbers):
    # Assume the first element is the max initially
    max_value = numbers[0]
    
    # Loop through the rest of the list
    for num in numbers[1:]:
        if num > max_value:
            max_value = num  # Update max_value if current num is bigger
    
    return max_value

# Take input as comma-separated numbers and convert to list of integers
input_numbers = input("Enter numbers separated by commas: ")
numbers_list = [int(x.strip()) for x in input_numbers.split(",")]

# Find max value
max_num = find_max_value(numbers_list)

print(f"The maximum value is: {max_num}")
