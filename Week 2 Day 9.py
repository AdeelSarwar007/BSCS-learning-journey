class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def show(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
s1 = Student("Adeel", 90)
s2 = Student("Ali", 85)
s3 = Student("Ahmed", 80)
s1.show()
print()

s2.show()
print()

s3.show()


        

