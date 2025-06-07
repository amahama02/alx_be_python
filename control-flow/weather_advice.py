# weather_advice.py

def get_clothing_recommendation():
    """
    Asks the user about the current weather conditions and provides clothing recommendations.
    """
    # Prompt the user for the weather input, ensuring it's stripped of whitespace and in lowercase
    weather=input("What's the weather like today? (sunny/rainy/cold):").strip().lower()

    # Provide clothing recommendations based on the user's input
    if weather=='sunny':
        print("Wear a t-shirt and sunglasses.")
    elif weather=='rainy':
        print("Don't forget your umbrella and a raincoat.")
    elif weather=='cold':
        print("Make sure to wear a warm coat and a scarf.")
    else:
        # Handle unexpected or invalid input
        print("Sorry, I don't have recommendations for this weather.")

# Main execution block: calls the function when the script is run directly
if __name__ == "__main__":
    get_clothing_recommendation()