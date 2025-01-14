class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.account_number = account_number
        self.balance = initial_balance

account = BankAccount("12345678", 1000)
print(f"account_number: {account.account_number}, balance: {account.balance}")
