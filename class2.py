class BankAccount:

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}")
        print(f"Current Balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn {amount}")
            print(f"Current Balance: {self.balance}")
        else:
            print("Insufficient Balance")

    def display(self):
        print("\nAccount Details")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.balance}")


# Create Object
acc1 = BankAccount("Kanna", 1000)

# Perform Operations
acc1.deposit(500)

acc1.withdraw(200)

acc1.display()


