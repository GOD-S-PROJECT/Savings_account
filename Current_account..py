class SavingsAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of ${amount} successful.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of ${amount} successful.")
        else:
            print("Insufficient funds for withdrawal.")

    def check_balance(self):
        print(f"Account balance: ${self.balance}")


# Example usage:
account = SavingsAccount(1000)  # Creating an account with an initial balance of $1000
account.check_balance()  # Output: Account balance: $1000

account.deposit(550)  # Deposit $550
account.check_balance()  # Output: Account balance: $550

account.withdraw(65)  # Withdraw $65
account.check_balance()  # Output: Account balance: $65

account.withdraw(100)  # Trying to withdraw $100 (insufficient funds)
account.check_balance()  # Output: Insufficient funds for withdrawal.