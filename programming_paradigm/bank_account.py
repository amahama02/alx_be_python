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
        Does NOT print success messages directly.

        Args:
            amount (float): The amount to deposit. Must be positive.
        
        Returns:
            bool: True if the deposit was successful, False otherwise.
        """
        if not isinstance(amount, (int, float)):
            # print("Deposit amount must be a number.") # Removed print
            return False # Indicate failure
        if amount <= 0:
            # print("Deposit amount must be positive.") # Removed print
            return False # Indicate failure

        self.account_balance += amount
        return True # Indicate success

    def withdraw(self, amount):
        """
        Deducts the specified amount from the account balance if funds are sufficient.
        Does NOT print success/failure messages directly, only returns status.

        Args:
            amount (float): The amount to withdraw. Must be positive.

        Returns:
            bool: True if the withdrawal was successful, False otherwise.
        """
        if not isinstance(amount, (int, float)):
            # print("Withdrawal amount must be a number.") # Removed print
            return False
        if amount <= 0:
            # print("Withdrawal amount must be positive.") # Removed print
            return False
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True # Indicate success
        else:
            return False # Indicate failure (insufficient funds)

    def display_balance(self):
        """
        Prints the current account balance in a user-friendly format.
        This method is still responsible for printing its output.
        """
        print(f"Current Balance: ${self.account_balance:.2f}")