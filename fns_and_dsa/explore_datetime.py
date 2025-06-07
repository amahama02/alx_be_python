# explore_datetime.py

# Import necessary modules
import datetime
from datetime import timedelta

def display_current_datetime():
    """
    Gets the current date and time, formats it, and prints it.

    Returns:
        datetime.datetime: The current datetime object.
    """
    # Part 1: Display the Current Date and Time
    current_date = datetime.datetime.now() # Get the current date and time

    # Format the datetime into "YYYY-MM-DD HH:MM:SS"
    formatted_current_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_current_datetime}")

    return current_date # Return the datetime object for future use

def calculate_future_date(start_date):
    """
    Prompts the user for a number of days, calculates a future date
    from the given start date, and prints it.

    Args:
        start_date (datetime.datetime): The datetime object from which to calculate the future date.
    """
    # Part 2: Calculate a Future Date
    while True:
        try:
            days_to_add_str = input("Enter the number of days to add to the current date: ")
            num_days = int(days_to_add_str) # Convert input to an integer
            break # Exit the loop if input is valid
        except ValueError:
            print("Invalid input. Please enter a whole number for days.")

    # Calculate the future date by adding the specified number of days.
    # We take just the date part of start_date if it includes time.
    future_date = start_date.date() + timedelta(days=num_days)

    # Format the future date into "YYYY-MM-DD"
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")

# Main block to execute the script
if __name__ == "__main__":
    # Display the current date and time and capture the datetime object
    current_dt_object = display_current_datetime()

    # Use the captured datetime object to calculate the future date
    calculate_future_date(current_dt_object)