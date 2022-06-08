
class BankAccount:

    def __init__(self, account_name, account_balance = 0, account_interest = 0.01):
        self.account_name = account_name
        self.account_balance = account_balance
        self.account_interest = account_interest

    def deposit(self, amount):
        self.account_balance += amount
        return self
    
    # Accepts an amount and subtracts that amount to the account's balance attribute

    def withdrawal(self, amount):
        self.account_balance -= amount
        return self

    # Prints balance of that account

    def display_account_info(self):
        print(f"Balance: {self.account_balance}")
        return self

    # Adds interest to account balannce by multiplying interest rate to current balance

    def yield_interest(self):
        self.account_balance += self.account_balance * self.account_interest
        return self

    # Creates three delicious BankAccount objects
    # With varying missing arguments

burrito = BankAccount("Beans", 1000, 0.02)
taco = BankAccount("Cheese", 2000)
taquito = BankAccount("Guacamole")

# Tests all instances of accounts with every method in the class BankAccount
print(burrito.account_name)
burrito.display_account_info().withdrawal(500).deposit(500).yield_interest().display_account_info()

print(taco.account_name)
taco.display_account_info().withdrawal(1500).deposit(500).yield_interest().display_account_info()

print(taquito.account_name)
taquito.display_account_info().withdrawal(2000).deposit(1000).yield_interest().display_account_info()