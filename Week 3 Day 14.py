name = input("Enter Name: ")

cnic = input("Enter CNIC Number: ")

try:
    marks = int(input("Enter Marks: "))

    if marks >= 50:
        print("Pass")
    else:
        print("Fail")

    if marks >= 80:
        print("Grade: A+")
    elif marks >= 60:
        print("Grade: B+")
    elif marks >= 40:
        print("Grade: C+")
    else:
        print("Grade: F")

except:
    print("Invalid Entry! Please enter numbers only.")
