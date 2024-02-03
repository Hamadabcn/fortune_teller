import random

def generate_prediction():
    predictions = [
        "\nYou will find unexpected success in the months ahead.\n",
        "\nTake risks and you will be greatly rewarded.\n",
        "\nTravel is on the horizon. Stay open to new experiences.\n",
        "\nA new opportunity will knock on your door this week.\n",
        "\nDon't be afraid to ask for help when needed.\n",
        "\nYour creativity will lead you to great achievements.\n",
        "\nEmbrace change, as it will bring you closer to your goals.\n",
        "\nToday is a lucky day. Trust your instincts.\n",
        "\nSuccess comes to those who work hard and persevere.\n",
        "\nTake time for self-care. It will rejuvenate your spirit.\n"
    ]

    return random.choice(predictions)

# Example usage
print("\nWelcome to the Random Prediction Generator!\n")

# Initialize user input
user_input = ""

# While loop to repeat the prediction process
while user_input != "q":
    # Generate and display prediction
    print("\nHere's your prediction: \n", generate_prediction())
    # Ask for user input
    user_input = input("\nEnter 'q' to quit or any other key to continue: ")
    