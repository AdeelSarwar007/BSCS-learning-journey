def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def divide(a, b):
    return a / b

print("---------Enter Choice for Operation---------")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exit")

choice = int(input("Enter Number: "))

if choice == 1:
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))
    print("Answer:", add(a, b))

elif choice == 2:
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))
    print("Answer:", sub(a, b))

elif choice == 3:
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))
    print("Answer:", mul(a, b))

elif choice == 4:
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))
    print("Answer:", divide(a, b))

elif choice == 5:
    print("Good Bye!")

else:
    print("Invalid Choice")
    