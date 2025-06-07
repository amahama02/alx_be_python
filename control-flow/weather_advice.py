# weather_advice.py

def get_weather_advice():
    """
    Asks the user about the current weather and provides clothing advice.
    """
    # Prompt the user for the weather input
    # .strip() removes leading/trailing whitespace
    # .lower() converts input to lowercase for consistent comparison
    weather=input("What's the weather like today? (sunny/rainy/cold):").strip().lower()

    # Provide advice based on the weather
    if weather=='sunny':
        print("Wear a t-shirt and sunglasses.")
    elif weather=='rainy':
        print("Take an umbrella and a raincoat.")
    elif weather=='snowy':
        print("Wear a warm coat and boots.")
    elif weather=='cloudy':
        print("A light jacket might be good.")
    else:
        print("Enjoy the day! I don't have specific advice for that weather.")

# Main block to run the function when the script is executed
if __name__ == "__main__":
    get_weather_advice()
