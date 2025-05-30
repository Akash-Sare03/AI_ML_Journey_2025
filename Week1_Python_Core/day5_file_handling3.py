
def append_to_file(filename, content):
    with open(filename, 'a') as f:
        f.write("\n" + content)

append_to_file("notes.txt", "This is an appended line.")
