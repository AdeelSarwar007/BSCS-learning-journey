note = input("Enter Note: ")

file = open("notes.txt", "w")

file.write(note)

file.close()

print("Note Saved!")