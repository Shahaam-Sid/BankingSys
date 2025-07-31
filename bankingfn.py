class BankingFn:
    def __init__(self, amount):
        self.amount = amount
        
    @property
    def amount(self):
        return self._amount
    
    @amount.setter
    def amount(self, value):
        if value >= 0:
            self._amount = value
        else:
            raise ValueError("Amount Cannot be Negative")
            
            
    def __repr__(self):
        return f"Amount({self._amount})"
    
class CheckBalance:
    def __init__(self, bal):
        self.bal = bal
        
    def __str__(self):
        return f"You Balance is ${self.bal:.2f}"
    


a = CheckBalance(200)
print(a)