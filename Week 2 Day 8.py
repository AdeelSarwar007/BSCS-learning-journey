class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

s1 = Student("Adeel", 90)
s2 = Student("Ali", 85)
s3 = Student("Ahmed", 80)

print(s1.name, s1.marks)
print(s2.name, s2.marks)
print(s3.name, s3.marks)