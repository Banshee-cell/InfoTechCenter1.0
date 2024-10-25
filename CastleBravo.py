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
