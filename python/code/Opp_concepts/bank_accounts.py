class BankAccount:
    def __init__(self , initial_amount , account_name):
        self.balance = initial_amount
        self.name = account_name
        print(f"\n Account '{self.name}' created.\nBalance = ${self.balance:.2f}")

    def get_balance(self):
        return f"\nAccount : '{self.name}' balance = ${self.balance}"
    
    def deposit(self ,amount):
        self.balance = self.balance + amount
        print("The deposit was successful")
        self.get_balance()