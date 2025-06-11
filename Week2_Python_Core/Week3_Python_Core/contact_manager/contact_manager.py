# contact_manager.py

import json
import os

# File to store contacts
FILE_NAME = "contacts.json"

# Load contacts from file
def load_contacts():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)

# Save contacts to file
def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        for index, contact in enumerate(contacts, start=1):
            print(f"{index}. Name: {contact['name']}")
            print(f"   Phone: {contact['phone']}")
            print(f"   Email: {contact['email']}")
            print(f"   Address: {contact['address']}")


def add_contact(contacts):
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    print(f"Contact '{name}' added successfully!")


def search_contact(contacts):
    search_term = input("Enter name or phone number to search: ")
    found = False  # Flag to check if any match was found

    for index, contact in enumerate(contacts, start=1):
        if search_term.lower() in contact['name'].lower() or search_term == contact["phone"]:
            print(f"{index}. Name: {contact['name']}")
            print(f"   Phone: {contact['phone']}")
            print(f"   Email: {contact['email']}")
            print(f"   Address: {contact['address']}")
            found = True

    if not found:
        print("No matching contact found.")


def update_contact(contacts):
    update = input("Enter name or phone number to update: ")
    found = False

    for contact in contacts:
        if update.lower() in contact["name"].lower() or update == contact["phone"]:
            print("Contact found. Leave blank to keep current values.")

            new_name = input(f"Enter new name (current: {contact['name']}): ")
            new_phone = input(f"Enter new phone (current: {contact['phone']}): ")
            new_email = input(f"Enter new email (current: {contact['email']}): ")
            new_address = input(f"Enter new address (current: {contact['address']}): ")

            if new_name:
                contact["name"] = new_name
            if new_phone:
                contact["phone"] = new_phone
            if new_email:
                contact["email"] = new_email
            if new_address:
                contact["address"] = new_address

            print("Contact updated successfully!")
            found = True
            break

    if not found:
        print("Contact not found.")


def delete_contact(contacts):
    delete = input("Enter name or phone number to delete: ")
    found = False

    for contact in contacts:
        if delete.lower() in contact["name"].lower() or delete == contact["phone"]:
            confirm = input("Are you sure you want to delete this contact? (yes/no): ")
            if confirm.lower() == "yes":
                contacts.remove(contact)
                print("Contact deleted successfully!")
            else:
                print("Deletion cancelled.")
            found = True
            break  # Stop after deleting

    if not found:
        print("Contact not found.")

# Show main menu
def show_menu():
    print("\n==== Contact Manager ====")
    print("1. View Contacts")
    print("2. Add Contact")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

# Main app loop
def main():
    contacts = load_contacts()
    
    while True:
        show_menu()
        choice = input("Choose an option (1-6): ")
        if choice == "1":
            view_contacts(contacts)
        elif choice == "2":
            add_contact(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            save_contacts(contacts)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
