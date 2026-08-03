class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show(self):
        print("Name:", self.name)
        print("Marks:", self.marks)


students = []

while True:

    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        name = input("Enter Name: ")
        marks = int(input("Enter Marks: "))

        student = Student(name, marks)

        students.append(student)

        print("Student Added Successfully!")

    elif choice == "2":

        if len(students) == 0:
            print("No Students Found!")

        else:
            print("\n----- Student List -----")

            for student in students:
                student.show()
                print()

    elif choice == "3":

        print("Good Bye!")
        break

    else:
        print("Invalid Choice!")