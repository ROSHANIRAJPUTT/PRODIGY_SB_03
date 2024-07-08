import json

# Define a function to load contacts from a file
def load_contacts(filename='contacts.json'):
    try:
        with open(filename, 'r') as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = []
    return contacts

# Define a function to save contacts to a file
def save_contacts(contacts, filename='contacts.json'):
    with open(filename, 'w') as file:
        json.dump(contacts, file, indent=4)

# Define a function to add a new contact
def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contact = {
        'name': name,
        'phone': phone,
        'email': email
    }
    contacts.append(contact)
    print("Contact added successfully.")

# Define a function to view all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        for idx, contact in enumerate(contacts):
            print(f"Contact {idx + 1}:")
            print(f"  Name: {contact['name']}")
            print(f"  Phone: {contact['phone']}")
            print(f"  Email: {contact['email']}")
            print("-" * 20)

# Define a function to edit a contact
def edit_contact(contacts):
    view_contacts(contacts)
    index = int(input("Enter the contact number to edit: ")) - 1
    if 0 <= index < len(contacts):
        name = input(f"Enter new name (leave blank to keep '{contacts[index]['name']}'): ")
        phone = input(f"Enter new phone number (leave blank to keep '{contacts[index]['phone']}'): ")
        email = input(f"Enter new email address (leave blank to keep '{contacts[index]['email']}'): ")
        
        if name:
            contacts[index]['name'] = name
        if phone:
            contacts[index]['phone'] = phone
        if email:
            contacts[index]['email'] = email
        
        print("Contact updated successfully.")
    else:
        print("Invalid contact number.")

# Define a function to delete a contact
def delete_contact(contacts):
    view_contacts(contacts)
    index = int(input("Enter the contact number to delete: ")) - 1
    if 0 <= index < len(contacts):
        contacts.pop(index)
        print("Contact deleted successfully.")
    else:
        print("Invalid contact number.")

# Define the main function to manage the menu
def main():
    contacts = load_contacts()
    
    while True:
        print("\nContact Manager")
        print("1. Add new contact")
        print("2. View contacts")
        print("3. Edit contact")
        print("4. Delete contact")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_contact(contacts)
            save_contacts(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            edit_contact(contacts)
            save_contacts(contacts)
        elif choice == '4':
            delete_contact(contacts)
            save_contacts(contacts)
        elif choice == '5':
            save_contacts(contacts)
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

# Run the program
if __name__ == '__main__':
    main()