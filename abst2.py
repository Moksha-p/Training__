from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process(self):
        pass

class CreditCard(Payment):
    def __init__(self, number):
        self.number = number

    def process(self):
        return f"Processing credit card payment for {self.number}"

class PayPal(Payment):
    def __init__(self, account):
        self.account = account

    def process(self):
        return f"Processing PayPal payment for {self.account}"

credit_card = CreditCard("1234")
paypal = PayPal("user@example.com")
print(credit_card.process())
print(paypal.process())