
from datetime import datetime

def write_entry():
    entry = input("Write your diary entry:\n")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # e.g., 2025-05-29 14:30:00
    with open("diary.txt", 'a') as File:
        File.write(f"{timestamp}\n{entry}\n---\n")
    print("Entry saved successfully!")    

def view_entries():
    try:
        with open("diary.txt", 'r') as File:
            content = File.read()
            print("\n Your Diary Entries: \n")
            print(content)
    except FileNotFoundError:
        print("No diary entries found yet.")

def search_entries():
    keyword = input("Enter the word to search for: ").lower()
    try:
        with open("diary.txt", 'r') as file:
            entries = file.read().lower()
            if keyword in entries:
                print(f"Entries containing '{keyword}':\n")
                # Split entries by separator and print matching ones
                for entry in entries.split('---'):
                    if keyword in entry:
                        print(entry.strip())
                        print("---")
            else:
                print(f"No entries found containing '{keyword}'.")
    except FileNotFoundError:
        print("No diary entries found yet.")


def diary_app():

    password = "1234"  # Change this to your desired password
    user_input = input("Enter the diary password: ")
    if user_input != password:
        print("Incorrect password. Access denied.")
        return  # Exit the app if password is wrong
    
    while True:
        print("\nDiary app menu:")
        print("1. Write new Entry")
        print("2. View all Entries")
        print("3. Search Entries")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4) :")
        
        if choice == '1':
            write_entry()
        elif choice == '2':
            view_entries()
        elif choice == '3':
            search_entries()    
        elif choice == '4':
            print("Goodbye! see you tomorrow.")
            break
        else:
            print("Invalid choice. please enter 1, 2, 3 or 4")
    
diary_app()


