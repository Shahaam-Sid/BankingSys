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
    
    
    
#test cases
a.amount = 10

print(a)    
    