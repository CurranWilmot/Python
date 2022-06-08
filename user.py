

class User:
    #Constructs user object and attributes
    def __init__(self, user_name, user_email, user_balance = 0):
        self.user_name = user_name
        self.user_email = user_email
        self.user_balance = user_balance

    # Accepts an amount and adds that amount to the user's balance attribute

    def make_deposit(self, amount):
        self.user_balance += amount
        return self
    
    # Accepts an amount and subtracts that amount to the user's balance attribute

    def make_withdrawal(self, amount):
        self.user_balance -= amount
        return self

    # Displays user's name and then prints balance of that user

    def display_user_balance(self):
        print(f"User: {self.user_name}, Balance: {self.user_balance}")
        return self

    # Uses make_withdrawal method to subtract an 'amount' from first user
    # Uses make_deposit method to add an 'amount' from second user

    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        return self

# Creates 3 instances of User object
        
monty = User("Monty", "Monty@python.net", 8000)
bob = User("Bob", "Bob@bobmail.com", 5000)
shirley = User("Shirley", "Shirley@youcannotbeserious.net", 1000000)

# Displays balances of all 3 instances of User object

monty.display_user_balance()
bob.display_user_balance()
shirley.display_user_balance()

# Series of transactions for all 3 Users that prints result

monty.make_deposit(100).make_deposit(100).make_deposit(100).make_withdrawal(200).display_user_balance()

bob.make_deposit(300).make_deposit(300).make_withdrawal(100).make_withdrawal(150).display_user_balance()

shirley.make_deposit(100000).make_withdrawal(50000).make_withdrawal(10000).make_withdrawal(30000).display_user_balance()

# Transfers 4000 from one user to another
# Displays new balances after

monty.transfer_money(shirley, 4000).display_user_balance()
shirley.display_user_balance()