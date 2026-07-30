students = []

def add_student():
    name = input("Enter Name: ")
    students.append(name)
    print("Student added successfully!")

def show_student():
    if not students:
        print("No students in the list yet.")
    else:
        print("\n--- Student List ---")
        for student in students:
            print(student)

        for i, student in enumerate(students, start=1):
            print(i, "-", student)

# ------- Menu Loop ---------
while True:
    print("\n1. Enter 1 to Add Student")
    print("2. Enter 2 to Show Students")
    print("3. Enter 3 to Exit")
    
    num = input("Enter number: ")
    
    if num == "1":
        add_student()
    elif num == "2":
        show_student()
    elif num == "3":
        print("Exiting program. Good luck!")
        break
    else:
        print("Invalid choice, please enter 1, 2, or 3.")
    