

import sys  # Importing the sys module for system-specific parameters and functions
import time  # Importing the time module to use time-related functions# import sys  # Importing the sys module for system-specific parameters and functions
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


# Print a decorative header for the output
print("\n**************************************\n")

# Indicate the type of application
print("Gasoline Branch")

# Import necessary libraries
import random  # For generating random values
from time import sleep  # For adding delays

# Function to get a random gas level from a predefined list
def gasLevelGauge():
    return random.choice(["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"])

# Function to select a random gas station from a list
def gasStations():
    return random.choice(["VP", "Shell", "Meijer", "Sams Club", "Marathon", "Mobile", "Speedway", "Circle K"])

# Function to get the distance to the nearest gas station based on gas level
def getDistance(gas_level):
    if gas_level in ["Empty", "Low"]:
        return random.uniform(1, 25)  # Distance for low levels
    elif gas_level == "Quarter Tank":
        return random.uniform(25.1, 50)  # Distance for quarter tank
    return None  # No distance needed for higher levels

# Function to check the gas level and provide alerts
def gasLevelAlert():
    gas_level = gasLevelGauge()  # Get the current gas level
    distance = getDistance(gas_level)  # Get the distance if applicable

    # Messages based on the gas level
    messages = {
        "Empty": "***WARNING - YOU ARE ON EMPTY***\nCalling Triple AAA",
        "Low": f"Your gas tank is extremely low, checking GPS for closest gas station\nThe closest gas station is {gasStations()}, which is {distance:.2f} miles away.",
        "Quarter Tank": f"Your gas tank is on a quarter of a tank, checking GPS for closest gas station\nThe closest gas station is {gasStations()}, which is {distance:.2f} miles away.",
        "Half Tank": "Your gas tank is half full which is plenty enough to get to your destination.",
        "Three Quarter Tank": "Your gas tank is three quarters full.",
        "Full Tank": "Your gas tank is full."
    }

    # Print the appropriate message
    print(messages[gas_level])
    if gas_level in ["Empty", "Low", "Quarter Tank"]:  # Add delay for warnings
        sleep(1.5)

# Call the gas level alert function to execute the code
gasLevelAlert()

