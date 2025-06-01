task = input("Enter your task description: ")
priority = input("Priority (high, medium, low): ")
time_bound = input("Is it time-bound? (yes/no): ")
reminder_message = "Reminder: "
match priority.lower(): 
    case "high":
        reminder_message += f"'{task}' is a high priority task."
    case "medium":
        reminder_message += f"'{task}' is a medium priority task."
    case "low":
        reminder_message += f"'{task}' is a low priority task."
    case _:
        reminder_message = "Sorry, I don't recognize this priority. "
        reminder_message += f"'{task}' needs to be done."

if time_bound.lower() == "yes": # Utilisez .lower() pour gérer les majuscules/minuscules
    reminder_message += " that requires immediate attention today!"
print(reminder_message)
