# This code simulates a vehicle response system based on weather conditions.

# Print some introductory formatting and messages
print("\n**********************\n")
print("Weather Branch\n")

# Import required libraries
import random  # For randomly selecting a weather condition
from time import sleep  # To simulate a delay in the system


# Function to randomly choose a weather condition from a predefined list
def weather():
    weatherForecast = ["snowy", "rainy", "blizzard", "windy", "icy", "sunny"]  # List of possible weather conditions
    return random.choice(weatherForecast)  # Randomly select and return a weather condition


# Get the current weather alert by calling the weather function
weatherAlert = weather()

# Dictionary mapping weather conditions to delay times and messages
weather_alerts = {
    "snowy": (30, "VRS system has been engaged only allowing you to drive 55mph."),
    "rainy": (5, ""),
    "blizzard": (60, ""),
    "windy": (10, ""),
    "icy": (50, "")
}


# Function to simulate the vehicle's response system based on weather conditions
def vehicleResponseSystem():
    # If the weather condition is in the dictionary, print corresponding messages
    if weatherAlert in weather_alerts:
        delay, extra_msg = weather_alerts[weatherAlert]  # Retrieve delay and extra message if any
        print(
            f"\nThe National Weather Service has updated our alarm by {delay} minutes because of the forecast of {weatherAlert} weather conditions.")

        if extra_msg:  # If there's an extra message, print it
            sleep(1)
            print(extra_msg)

    # If the weather is sunny, no special action is required
    else:
        print(f"\nThe National Weather Service has turned off because of {weatherAlert} skies.")


# Call the vehicle response system function to check the response based on the current weather alert
vehicleResponseSystem()
