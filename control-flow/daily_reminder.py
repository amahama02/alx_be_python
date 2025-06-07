
def create_daily_reminder():
    task = input("Enter your task description: ").strip()
    while True:
        priority = input("Enter priority (high, medium, low): ").strip().lower()
        if priority in ['high', 'medium', 'low']:
            break
        else:
            print("Invalid priority. Please choose 'high', 'medium', or 'low'.")
    while True:
        time_bound = input("Is this task time-bound? (yes/no): ").strip().lower()
        if time_bound in ['yes', 'no']:
            break
        else:
            print("Invalid input. Please answer 'yes' or 'no'.")
    reminder_message = f"Reminder: '{task}' is a {priority} priority task"

    match priority:
        case 'high':
            # Add specific advice for high priority
            reminder_message += " that needs to be done urgently."
        case 'medium':
            # Add specific advice for medium priority
            reminder_message += " that you should get to soon."
        case 'low':
            # Add specific advice for low priority
            reminder_message += " that can be done when you have free time."
        # The '_' case catches anything else, though our validation should prevent it.
        case _:
            reminder_message += "." # Default ending if priority is unexpected)
    if time_bound == 'yes':
        # Add the specific time-sensitive phrase
        reminder_message += " That requires immediate attention today!"

    print(reminder_message)

# Ensure the function runs when the script is executed
if __name__ == "__main__":
    create_daily_reminder()
