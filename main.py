#main file
from bankingfn import *

balance = 100
choice = 0
isRunning = True

print("----------BANKING PROGRAM---------")


while isRunning:
    
    print("""Enter:
1, to check balance
2, to deposit
3, to withdraw
4, to exit
""")

    choice = input("Enter your Choice: ")

    match choice:
        case "1":
            a = CheckBalance(balance)
            print(a)
        
        
        case "2":
            try:
                b = Deposit(int(input("Enter Amount: ")))
                balance += b.amount
                print("Deposit Successful")
            except ValueError:
                print("Value must be A Positive Integer")
            except Exception:
                print("An Error Occured, Try Again")
           
            
        case "3":
            try:
                c = Withdraw(int(input("Enter Amount: ")), balance)
                balance -= c.amount
                print("Withdrawal Successful")
            except ValueError:
                print("Value must be Positive and Lesser then your Current Balance")
            except Exception:
                print("An Error Occured, Try Again")
          
            
        case "4":
            isRunning = False
            
            
        case _:
            print("Wrong Option, Try Again")

print("----------------------------------")