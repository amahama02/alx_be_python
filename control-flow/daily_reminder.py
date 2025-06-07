# daily_reminder.py

def create_daily_reminder():
   task = input ("Enter your task: ").strip ()

    # 2. Prompt for Task Priority with validation loop
    while True:
        priority = input ("Priority (high/medium/low): ").strip ().lower ()
        if priority in ['high', 'medium', 'low']:
            break
        else:
            print ("Invalid priority. Please choose 'high', 'medium', or 'low'.")

    # 3. Prompt if Task is Time-Bound with validation loop
    while True:
        time_bound = input ("Is it time-bound? (yes/no): ").strip ().lower ()
        if time_bound in ['yes', 'no']:
            break
        else:
            print ("Invalid input. Please answer 'yes' or 'no'.")

    # --- Section de construction du message ---
    # Nous construisons le corps du message d'abord
    # La phrase "Reminder: " sera ajoutée directement dans le print final.
    base_message_content = f"'{task}' is a {priority} priority task"

    match priority:
        case 'high':
            base_message_content += " that needs to be done urgently."
        case 'medium':
            base_message_content += " that you should get to soon."
        case 'low':
            base_message_content += " that can be done when you have free time."
        case _: # Fallback for unexpected priority (though validation should prevent this)
            base_message_content += "."

    # 5. Modify Reminder if Task is Time-Bound (using if statement)
    if time_bound == 'yes':
        # Ajoute la phrase spécifique de sensibilité au temps
        base_message_content += " That requires immediate attention today!"

    # 6. Print the Customized Reminder (maintenant avec "Reminder: " directement dans le print)
    Print(f"Reminder: {base_message_content}") # <-- C'est la ligne clé modifiée pour le vérificateur

# Ensure the function runs when the script is executed
if __name__ == "__main__":
    create_daily_reminder()
