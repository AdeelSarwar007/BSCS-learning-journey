contacts = {
    "Ali": "03111234567",
    "Ahmed": "03001234567"
}

while True:
    print("\n===== Contact Book =====")
    print("1. Add Contact")
    print("2. Show Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        number = input("Enter Number: ")

        contacts[name] = number
        print("Contact Added Successfully!")

    elif choice == "2":
        print("\n--- Contact List ---")

        if not contacts:
            print("No Contacts Found")
        else:
            for name, number in contacts.items():
                print(name, ":", number)

    elif choice == "3":
        search_name = input("Enter Name to Search: ")

        if search_name in contacts:
            print("Number:", contacts[search_name])
        else:
            print("Contact Not Found")

    elif choice == "4":
        print("Exiting Contact Book...")
        break

    else:
        print("Invalid Choice!")
