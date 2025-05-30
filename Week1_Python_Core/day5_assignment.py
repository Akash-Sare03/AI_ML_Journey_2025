
from datetime import datetime

def append_entry():
    entry_text = input("Write your entry:\n")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # e.g., 2025-05-29 14:30:00
    with open("log.txt", 'a') as File:
        File.write(f"{timestamp}\n{entry_text}\n---\n")
    print("Entry saved successfully! ✅")

def display_entries():
    try:
        with open("log.txt", 'r') as File:
            content = File.read()
            print("\nYour Entries:\n")
            print(content)
    except FileNotFoundError:
        print("No entries found.")

append_entry()
display_entries()

