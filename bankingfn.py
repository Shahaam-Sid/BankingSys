#class file
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
            raise ValueError("Value must be positive")
            
            
    def __repr__(self):
        return f"Amount({self._amount})"
    
class CheckBalance:
    def __init__(self, bal):
        self.bal = bal
        
    def __str__(self):
        return f"You Balance is ${self.bal:.2f}"
    
    
class Deposit(BankingFn):
    pass

class Withdraw(BankingFn):
    def __init__(self, amount, bal):
        self.bal = bal
        super().__init__(amount)

        

    @BankingFn.amount.setter
    def amount(self, value):
        if value >= 0 and value <= self.bal:
            self._amount = value
        else:
            raise ValueError("Value must be Positive and Lesser then your Current Balance")
            
            
    def __repr__(self):
        return f"Amount({self._amount}), Balance({self.bal})"