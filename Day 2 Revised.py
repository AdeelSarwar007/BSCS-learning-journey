# Part 1: Function Example (Area Calculator)
def calculate_area(length, width):
    Area = length * width
    return Area

length = int(input("Enter length: "))
width = int(input("Enter Width: "))
print(calculate_area(length, width))


# Part 2: OOP Example (BankAccount)
class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Rs. {amount} deposit ho gaye hain. Naya balance: Rs. {self.balance}")
        else:
            print("Deposit amount positive hona chahiye!")

account1 = BankAccount(1000)
account1.deposit(500)
account1.deposit(-200)


# Part 3: Error Handling Example (Division)
try:
    num1 = int(input("Pehla number: "))
    num2 = int(input("Doosra number: "))
    result = num1 / num2
    print(result)
except:
    print("Zero se divide nahi ho sakta!")




     