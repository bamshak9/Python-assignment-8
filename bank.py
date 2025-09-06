"""
TASK: Create a BankAccount class.

Requirements:
1. Each account should have an owner name and a starting balance.
2. Provide a method to deposit money.
3. Provide a method to withdraw money (only if sufficient balance).
4. Provide a method to check current balance.

Example Usage:
    acc = BankAccount("Alice", 1000)
    acc.deposit(500)
    acc.withdraw(200)
    print(acc.get_balance())  # 1300
"""
class BankAccount:
    def __init__(self, name, starting_balance):
        self.account={name:starting_balance}
        self.name=name
        self.starting_balance=starting_balance
    def deposit(self,amount):
        self.account[self.name]+=amount
        print("Money succesfully added")
    def withdraw(self,amount):
        if amount>self.account[self.name]:
            print("You have an insufficient account balance")
        else:
            self.account[self.name]-=amount
            print("Money succesfully withdrawn")
    def get_balance(self):
        return self.account.get(self.name)


acc = BankAccount("Alice", 1000)
acc.deposit(500)
acc.withdraw(200)
print(acc.get_balance())