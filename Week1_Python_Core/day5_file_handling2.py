
def read_from_file(filename):
    with open(filename, 'r') as f:
        return f.read()
    
text = read_from_file("notes.txt")

print(text)
    