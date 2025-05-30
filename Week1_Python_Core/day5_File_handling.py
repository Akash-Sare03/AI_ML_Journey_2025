
#  Write to a File

def write_to_file(filename, content):
    with open(filename, 'w') as f:
        f.write(content)

write_to_file("notes.txt", "Today I learned file handling in Python.")


