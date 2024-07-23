from bank_accounts import *

billy = BankAccount(735364,"Billy")
abongile = BankAccount(846353873,"Abongile")
ifalanga = BankAccount(6453,"ifalanga")

print(billy.get_balance())
billy.deposit(4773552)
print(billy.get_balance())