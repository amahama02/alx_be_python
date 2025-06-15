def safe_divide(numerator, denominator):
    """
    Performs division of two numbers, robustly handling potential errors.

    Args:
        numerator: The number to be divided.
        denominator: The number by which to divide.

    Returns:
        str: A message indicating the result of the division or an error.
    """
    try:
        # Attempt to convert inputs to float
        num = float(numerator)
        den = float(denominator)

        # Check for division by zero after conversion
        if den == 0:
            return "Error: Cannot divide by zero."

        # Perform division
        result = num / den
        # --- C'EST LA LIGNE MODIFIÉE ---
        return f"The result of the division is {result}"
    except ValueError:
        # Catch error if conversion to float fails (non-numeric input)
        return "Error: Please enter numeric values only."