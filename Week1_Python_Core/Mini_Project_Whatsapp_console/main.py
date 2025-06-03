

users = []

def signup():
    username = input("Enter a new username: ").strip()
    if username in users:
        print("Username already exists! Try again.")
    else:
        users.append(username)
        print(f"User '{username}' created successfully!")


def login():
    username = input("Enter your username: ").strip()
    if username in users:
        print(f"Logged in as: {username}")
        return username
    else:
        print("Username not found! Please sign up first.")
        return None
    
def main_menu():
    while True:
        print("\n📱 Welcome to WhatsApp Console App")
        print("1. Login")
        print("2. Sign up")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == '1':
            user = login()
            if user:
                print(f"✅ Welcome back, {user}!")
                break  # Exit loop after successful login
        elif choice == '2':
            signup()
        elif choice == '3':
            print("👋 Goodbye!")
            break  # Exit loop on user request
        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main_menu()

def send_message(sender):
    recipient = input("Enter recipient username: ").strip()
    if recipient not in users:
        print("❌ User not found!")
        return

    msg = input("Enter your message: ").strip()
    full_message = f"{sender} ➜ {msg}"

    if recipient not in messages:
        messages[recipient] = []

    messages[recipient].append(full_message)
    print("✅ Message sent!")

def check_inbox(username):
    print(f"\n📥 {username}'s Inbox:")
    inbox = messages.get(username, [])
    if not inbox:
        print("No messages.")
    else:
        for msg in inbox:
            print(f"- {msg}")

def view_users(current_user):
    print("\n Available Users:")
    for user in users:
        if user != current_user:
            print(f"- {user}")

def delete_message(username):
    # Get the user's inbox messages, or empty list if none
    inbox = messages.get(username, [])
    
    # If inbox is empty, inform and return
    if not inbox:
        print("No messages to delete.")
        return
    
    # Print all messages with numbers
    print("\nYour Messages:")
    for index, msg in enumerate(inbox, start=1):
        print(f"{index}. {msg}")
    
    # Ask user which message number to delete
    choice = int(input("Enter message number to delete: "))
    
    # Validate choice
    if 1 <= choice <= len(inbox):
        # Remove chosen message (index in list is choice - 1)
        deleted_msg = inbox.pop(choice - 1)
        print(f"Deleted message: {deleted_msg}")
        
        # Update messages dictionary
        messages[username] = inbox
    else:
        print("Invalid message number.")


def main_menu(username):
    while True:
        print("\nMain Menu:")
        print("1. View Users")
        print("2. Send Message")
        print("3. Delete Message")
        print("4. Logout")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            view_users(username)
        elif choice == '2':
            send_message(username)
        elif choice == '3':
            delete_message(username)
        elif choice == '4':
            print(f"Logging out {username}...")
            break
        else:
            print("Invalid choice, please try again.")
