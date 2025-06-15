class BankAccount:
    """
    Represents a simple bank account with deposit, withdrawal,
    and balance display functionalities.
    """
    def __init__(self, initial_balance=0):
        """
        Initializes a new bank account with an optional initial balance.

        Args:
            initial_balance (float, optional): The starting balance for the account. Defaults to 0.
        """
        if not isinstance(initial_balance, (int, float)):
            raise TypeError("Initial balance must be a number.")
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.account_balance = initial_balance

    def deposit(self, amount):
        """
        Adds the specified amount to the account balance.

        Args:
            amount (float): The amount to deposit. Must be positive.
        """
        if not isinstance(amount, (int, float)):
            print("Deposit amount must be a number.")
            return
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.account_balance += amount
        print(f"Deposited ${amount:.2f}. New balance: ${self.account_balance:.2f}.")

    def withdraw(self, amount):
        """
        Deducts the specified amount from the account balance if funds are sufficient.

        Args:
            amount (float): The amount to withdraw. Must be positive.

        Returns:
            bool: True if the withdrawal was successful, False otherwise.
        """
        if not isinstance(amount, (int, float)):
            print("Withdrawal amount must be a number.")
            return False
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.account_balance:.2f}.")
            return True
        else:
            print("Insufficient funds.")
            return False

    def display_balance(self):
        """
        Prints the current account balance in a user-friendly format.
        """
        print(f"Your current balance is: ${self.account_balance:.2f}.")