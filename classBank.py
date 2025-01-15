class BankAccount :
    def __init__(self , account_number , initial_balance ):
        self.account_number = account_number
        self.initial_balance = initial_balance
bank = BankAccount("12345678" , 1000)
print(f"account_number: {bank.account_number} ,balance: {bank.initial_balance}")   
        