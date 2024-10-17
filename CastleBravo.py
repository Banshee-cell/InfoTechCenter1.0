
import sys  # Importing the sys module for system-specific parameters and functions
import time  # Importing the time module to use time-related functionsimport sys  # Importing the sys module for system-specific parameters and functions
import time  # Importing the time module to use time-related functions

# ANSI escape codes for colors
class TextColors:
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    RESET = '\033[0m'  # Reset color

# Welcome message for the user
print(f"\n{TextColors.CYAN}Welcome to InfoTechCenter V1.0{TextColors.RESET}\n")

# Initialize counters for the boot process
x = 0  # Counter for booting iterations
ellipsis = 0  # Counter for the ellipsis effect

timetosleep=4 # variable to et the time library to 4 seconds when called
time.sleep(timetosleep) # calling the time to sleep library with the variable time


# Loop to simulate the system booting process
while x != 20:
    x += 1  # Increment the boot counter
    # Create a booting message with an ellipsis effect and cyan color
    message = f"{TextColors.CYAN}InfoTech Center System Booting" + "." * ellipsis + f"{TextColors.RESET}"
    ellipsis += 1  # Increment the ellipsis counter
    sys.stdout.write("\r" + message)  # Overwrite the current line with the message
    time.sleep(0.5)  # Pause for half a second

    # Reset ellipsis counter after reaching 4 dots
    if ellipsis == 4:
        ellipsis = 0

    # Check if the boot process is complete
    if x == 20:

        # Green color for the final success message
        print(f"\n\n{TextColors.GREEN}Operating System Booted Up - Retina Scanned - Access Granted{TextColors.RESET}")

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

