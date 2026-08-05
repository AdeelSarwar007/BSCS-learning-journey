note = input("Enter Note: ")

file = open("notes.txt", "a")

file.write(note + "\n")

file.close()

print("Note Added Successfully!")