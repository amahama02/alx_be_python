# shopping_list_manager.py

def display_menu():
    """Displays the main menu options to the user."""
    print("--- Shopping List Manager ---")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    print("----------------------------")

def main():
    """Manages the shopping list based on user input."""
    shopping_list = [] # Initialize an empty list to store shopping items

    while True: # Loop continuously until the user chooses to exit
        display_menu() # Show the menu
        choice = input("Enter your choice: ").strip() # Get user's choice and remove whitespace

        if choice == '1':
            # --- Add Item functionality ---
            item_to_add = input("Enter the item to add: ").strip()
            if item_to_add: # Ensure the item name is not empty
                shopping_list.append(item_to_add) # Add the item to the list
                print(f"'{item_to_add}' has been added to your list.")
            else:
                print("Item name cannot be empty.")

        elif choice == '2':
            # --- Remove Item functionality ---
            if not shopping_list: # Check if the list is empty first
                print("Your shopping list is empty. Nothing to remove.")
                continue # Go back to the menu
            
            item_to_remove = input("Enter the item to remove: ").strip()
            if item_to_remove:
                # Use a try-except block to handle cases where the item is not found
                try:
                    shopping_list.remove(item_to_remove) # Attempt to remove the item
                    print(f"'{item_to_remove}' has been removed from your list.")
                except ValueError: # Catch the error if the item is not in the list
                    print(f"'{item_to_remove}' was not found in your list.")
            else:
                print("Item name cannot be empty.")

        elif choice == '3':
            # --- View List functionality ---
            if not shopping_list: # Check if the list is empty
                print("Your shopping list is empty.")
            else:
                print("\n--- Your Shopping List ---")
                # Loop through the list to display each item with its number
                for index, item in enumerate(shopping_list):
                    print(f"{index + 1}. {item}") # Display items starting from 1
                print("--------------------------")

        elif choice == '4':
            # --- Exit functionality ---
            print("Exiting Shopping List Manager. Goodbye!")
            break # Exit the while loop, ending the program

        else:
            # --- Handle invalid choices ---
            print("Invalid choice. Please enter a number between 1 and 4.")

# This ensures main() is called only when the script is executed directly
if __name__ == "__main__":
    main()