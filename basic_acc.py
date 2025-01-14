class BankAcc:
    def __init__(self,acct_no , inital_bal):
        self.account_nuber = acct_no
        self.initial_balance = inital_bal
    def credit(self , crd_amt):
        self.initial_balance += crd_amt
    def debit(self,dbt_amt):
        self.initial_balance -= dbt_amt

    def __repr__(self):
        return f"account_number: {self.account_nuber} , balance: {self.initial_balance}"
    
    

t4 = BankAcc(acct_no = "12345678", inital_bal = 1000)
# t4.credit(crd_amt=5000)
t4.debit(dbt_amt=3000)
print(t4)