

# arithmetic_operations.py

def perform_operation(num1, num2, operation):
    """
    Performs basic arithmetic operations based on the given numbers and operation type.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The type of operation ('add', 'subtract', 'multiply', 'divide').

    Returns:
        float or str: The result of the operation, or an error message for division by zero.
    """
    if operation =='add':
            return num1 + num2
        elif operation == 'subtract':
            return num1 - num2
        elif operation == 'multiply':
            return num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                return "Cannot divide by zero."
            else:
                return num1 / num2
        else _:
            return "Invalid operation type."