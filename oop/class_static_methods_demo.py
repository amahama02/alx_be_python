class Calculator:
    """
    A simple calculator class demonstrating the use of static and class methods.
    """
    # Class Attribute: Shared by all instances of the class
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        A static method that returns the sum of two numbers.
        It does not access any instance or class-specific data.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        A class method that returns the product of two numbers.
        It accesses a class attribute (calculation_type) via the 'cls' parameter.
        """
        print(f"Calculation type: {cls.calculation_type}") # Accessing class attribute via 'cls'
        return a * b