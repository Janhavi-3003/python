#4th program:"The common elements between two lists are"
"""list1 = list(map(int, input("Enter the first list of numbers separated by space: ").split()))
list2 = list(map(int, input("Enter the second list of numbers separated by space: ").split()))
for common_elements in list1:
    if common_elements in list2:
        print("The common elements between two lists are:", common_elements)(3 min)
#3rd program checkif a string is valid email
import re
def is_valid_email(email):
    email_re = r"^[a-zA-Z0-9._%+-]+@[a-zA-z.0-9-]+\.[a-zA-Z]{2,}$"
    if re.match(email_re, email):
        return True
    else:
        return False
email = input("Enter an email address: ")
if is_valid_email(email):
    print("Valid email address")
else:
    print("Invalid email address")"""
#7th program BANK ACCOUNT:
class Bank_Account:
    def __init__(self, account_number, account_name, initial_balance=0):
        self.account_number = account_number
        self.account_name = account_name
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit successful. New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal successful. New balance: ${self.balance:.2f}")
        else:
            print("Insufficient balance.")

    def check_balance(self):
        print(f"Current balance: ${self.balance:.2f}")

account_number = input("Enter account number: ")
account_name = input("Enter account name: ")
initial_balance = (input("Enter initial balance: "))

account = Bank_Account(account_number, account_name, initial_balance)

while True:
    print("\nBank Account Menu:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)
    elif choice == "2":
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)
    elif choice == "3":
        account.check_balance()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")

