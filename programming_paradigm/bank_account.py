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
        # Corrected print format to match "Deposited: $67.0"
        print(f"Deposited: ${amount:.1f}")

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
            # The problem description didn't specify output for withdraw,
            # but usually a success message is printed.
            print(f"Withdrew: ${amount:.1f}") # Added for clarity, format for consistency
            return True
        else:
            print("Insufficient funds.")
            return False

    def display_balance(self):
        """
        Prints the current account balance in a user-friendly format,
        including the specific phrase "Current Balance:".
        """
        # Corrected print format to match "Current Balance:"
        print(f"Current Balance: ${self.account_balance:.2f}")