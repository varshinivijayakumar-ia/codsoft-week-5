contacts = []
def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    address = input("Address: ")
    contacts.append({'name': name, 'phone': phone, 'email': email, 'address': address})
def view_contacts():
    for c in contacts:
        print(f"{c['name']} - {c['phone']}")
while True:
    print("\n1. Add\n2. View\n3. Exit")
    choice = input("Choose: ")
    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        break
