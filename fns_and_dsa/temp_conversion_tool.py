
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """
    Converts a temperature from Fahrenheit to Celsius.
    Utilizes the global FAHRENHEIT_TO_CELSIUS_FACTOR.

    Args:
        fahrenheit (float): The temperature in Fahrenheit.

    Returns:
        float: The converted temperature in Celsius.
    """
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """
    Converts a temperature from Celsius to Fahrenheit.
    Utilizes the global CELSIUS_TO_FAHRENHEIT_FACTOR.

    Args:
        celsius (float): The temperature in Celsius.

    Returns:
        float: The converted temperature in Fahrenheit.
    """
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

if __name__ == "__main__":
    # Loop to ensure a valid numeric temperature input
    while True:
        try:
            temp_input = input("Enter the temperature to convert: ")
            temperature = float(temp_input) # Attempt to convert input to a float
            break # Exit loop if conversion is successful
        except ValueError:
            # Handle cases where input is not a valid number
            print("Invalid temperature. Please enter a numeric value.")

    # Loop to ensure a valid unit input (C or F)
    while True:
        # Get unit from user, remove whitespace, and convert to uppercase for easy comparison
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        if unit in ['C', 'F']:
            break # Exit loop if unit is valid
        else:
            # Inform user about invalid unit
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    # Perform the conversion based on the chosen unit and display the result
    if unit == 'C':
        # If input is Celsius, convert to Fahrenheit
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted_temp}°F")
    elif unit == 'F':
        # If input is Fahrenheit, convert to Celsius
        converted_temp = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted_temp}°C")