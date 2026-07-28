# Function example
def greet(name):
    print(f"Hello {name}, welcome")

def add_numbers(a, b):
    return a + b

greet("Adeel")
result = add_numbers(10, 5)
print(f"Sum hai: {result}")

class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print(f"Mera naam {self.name} hai, age {self.age} hai, aur main {self.course} kar raha hoon.")
student1 = Student("Adeel", 20, "BSCS")
student1.introduce()