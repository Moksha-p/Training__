class Account:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance

account = Account("987654321", 5000)
account.deposit(1500)
account.withdraw(2000)
print(f"account_number: {account._Account__account_number}, balance: {account.get_balance()}")
