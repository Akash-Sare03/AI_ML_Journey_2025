
file = open("sample.txt", "r")   # Open the file in read mode
content = file.read()            # Read the whole content
print(content)                   # Print it
file.close()


file = open("sample.txt", "r")
line1 = file.readline()  # Reads first line
line2 = file.readline()  # Reads second line
print("Line 1:", line1)
print("Line 2:", line2)
file.close()



file = open("sample.txt", "r")
lines = file.readlines()   # Returns a list of lines
for line in lines:
    print(line.strip())    # .strip() removes \n
file.close()



file = open("sample.txt", "w")       # Open in write mode (overwrite)
file.write("This is new content.\n")
file.write("It replaces old content.\n")
file.close()


file = open("sample.txt", "a")      # Open in append mode
file.write("This line is appended.\n")
file.close()


## Reading & writing a file with 'with'

with open("sample.txt", "r") as file:
    content = file.read()
    print(content)


with open("sample.txt", "w") as file:
    file.write("Writing with 'with' statement is safer.\n")


try:
    with open("nofile.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Oops! The file does not exist.")
except Exception as e:
    print("Something went wrong:", e)


### Writing to a CSV file

import csv

# Sample data as list of lists (rows)
data = [
    ["Name", "Age", "City"],
    ["Alice", 25, "New York"],
    ["Bob", 30, "London"],
    ["Charlie", 22, "Paris"]
]

with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)


with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


## CSV using dictionary style

data = [
    {"Name": "Alice", "Age": 25, "City": "New York"},
    {"Name": "Bob", "Age": 30, "City": "London"},
    {"Name": "Charlie", "Age": 22, "City": "Paris"}
]

with open("data_dict.csv", "w", newline="") as file:
    fieldnames = ["Name", "Age", "City"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()           # Write the header row
    writer.writerows(data)          # Write the data rows



with open("data_dict.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)   # Each row is an OrderedDict (like a dictionary)


## Working with JSON Files in Python

import json

data = {
    "employees": [
        {"name": "Alice", "age": 25, "city": "New York"},
        {"name": "Bob", "age": 30, "city": "London"},
        {"name": "Charlie", "age": 22, "city": "Paris"}
    ]
}

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)  # indent=4 for pretty formatting

import json

with open("data.json", "r") as file:
    data = json.load(file)

print(data)

