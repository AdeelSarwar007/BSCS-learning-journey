Name = input("Enter Name: ")
Age = int(input("Enter Age: "))
Marks = int(input("Enter Marks: "))

print("\nStudent:", Name)
print("Age:", Age)
print("Marks:", Marks)

# CNIC Check
if Age >= 18:
    print("CNIC Status: Eligible")
else:
    print("CNIC Status: Not Eligible")

# Grade Check
if Marks >= 80:
    print("Grade: A")
elif Marks >= 70:
    print("Grade: B")
elif Marks >= 60:
    print("Grade: C")
elif Marks >= 50:
    print("Grade: D")
else:
    print("Grade: F")

# Pass/Fail Check
if Marks >= 50:
    print("Result: Pass")
else:
    print("Result: Fail")


