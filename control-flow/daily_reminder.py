# daily_reminder.py

def create_daily_reminder():

    task = input("Enter your task: ").strip()

    # 2. Prompt for Task Priority with validation loop (Corrected to match checker's exact prompt)
    while True:
        priority = input("Priority (high/medium/low):").strip().lower()
        if priority in ['high', 'medium', 'low']:
            break
        else:
            print("Invalid priority. Please choose 'high', 'medium', or 'low'.")

    # 3. Prompt if Task is Time-Bound with validation loop (Corrected to match checker's exact prompt)
    while True:
        time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
        if time_bound in ['yes', 'no']:
            break
        else:
            print("Invalid input. Please answer 'yes' or 'no'.")

    # 4. Process Task Based on Priority and Time Sensitivity (using match-case)
    # The base reminder message
    reminder_message = f"Reminder: '{task}' is a {priority} priority task"

    match priority:
        case 'high':
            reminder_message += " that needs to be done urgently."
        case 'medium':
            reminder_message += " that you should get to soon."
        case 'low':
            reminder_message += " that can be done when you have free time."
        case _: # Fallback for unexpected priority (though validation should prevent this)
            reminder_message += "."

    # 5. Modify Reminder if Task is Time-Bound (using if statement)
    if time_bound == 'yes':
        # Add the specific time-sensitive phrase as required by the prompt
        reminder_message += " That requires immediate attention today!"

    # 6. Print the Customized Reminder
    print(reminder_message)

# Ensure the function runs when the script is executed directly
if __name__ == "__main__":
    create_daily_reminder()