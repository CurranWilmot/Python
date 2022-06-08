class BankAccount:

    def __init__(self,account_balance = 0, account_interest = 0.02):
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

class User:
    #Constructs user object and attributes
    def __init__(self, user_name, user_email):
        self.user_name = user_name
        self.user_email = user_email
        self.account = BankAccount()

    # Accepts an amount and adds that amount to the user's balance attribute

    def make_deposit(self, amount):
        self.account.account_balance += amount
        return self
    
    # Accepts an amount and subtracts that amount to the user's balance attribute

    def make_withdrawal(self, amount):
        self.account.account_balance -= amount
        return self

    # Displays user's name and then prints balance of that user

    def display_user_balance(self):
        print(f"User: {self.user_name}, Balance: {self.account.account_balance}")
        return self

    # Uses make_withdrawal method to subtract an 'amount' from first user
    # Uses make_deposit method to add an 'amount' from second user

    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        return self

monty = User("Monty", "Monty@python.net")
bob = User("Bob", "Bob@bobmail.com")
shirley = User("Shirley", "Shirley@youcannotbeserious.net")

# Displays balances of all 3 instances of User object

monty.display_user_balance()
bob.display_user_balance()
shirley.display_user_balance()

# Series of transactions for all 3 Users that prints result

monty.make_deposit(100).make_deposit(100).make_deposit(100).make_withdrawal(200).display_user_balance()

bob.make_deposit(300).make_deposit(300).make_withdrawal(100).make_withdrawal(150).display_user_balance()

shirley.make_deposit(100000).make_withdrawal(50000).make_withdrawal(10000).make_withdrawal(30000).display_user_balance()

monty.transfer_money(shirley, 4000).display_user_balance()
shirley.display_user_balance()