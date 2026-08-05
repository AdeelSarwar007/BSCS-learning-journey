while True:

    print("\n===== Notes App =====")
    print("1. Add Note")
    print("2. Show Notes")
    print("3. Exit")
    print("4. Clear Notes")

    choice = input("Enter Choice: ")

    if choice == "1":

        note = input("Enter Note: ")

        file = open("notes.txt", "a")

        file.write(note + "\n")

        file.close()

        print("Note Added Successfully!")

    elif choice == "2":

        try:
            file = open("notes.txt", "r")

            print("\n----- Your Notes -----")
            print(file.read())

            file.close()

        except:
            print("No Notes Found!")

    elif choice == "3":

        print("Good Bye!")
        break
    elif choice=="4":
        file = open("notes.txt", "w")
        file.close()
        print("Notes Clean")

    else:
        print("Invalid Choice!")



    