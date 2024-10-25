# Print a decorative header for the output
print("\n**************************************\n")

# Indicate the type of application
print("Gasoline Branch")

# Import necessary libraries
import random  # For generating random values
from time import sleep  # For adding delays

# Function to get a random gas level from a predefined list
def gasLevelGauge():
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    return random.choice(gasLevelList)  # Return a random gas level

# Function to select a random gas station from a list
def gasStations():
    listOfGasStations = ["VP", "Shell", "Meijer", "Sams Club", "Marathon", "Mobile", "Speedway", "Circle K"]
    return random.choice(listOfGasStations)  # Return a random gas station name

# Function to check the gas level and provide alerts
def gasLevelAlert():
    # Generate random distances to gas stations based on the gas level
    milesToGasStationLow = random.uniform(1, 25)  # Distance for low gas level
    milesToGasStationQuarterTank = random.uniform(25.1, 50)  # Distance for quarter tank

    # Get the current gas level
    gasLevelIndicator = gasLevelGauge()

    # Check the gas level and respond accordingly
    if gasLevelIndicator == "Empty":
        print("***WARNING - YOU ARE ON EMPTY***\n")  # Alert for empty tank
        sleep(1.5)  # Pause for dramatic effect
        print("Calling Triple AAA")  # Simulate calling for assistance
    elif gasLevelIndicator == "Low":
        print("Your gas tank is extremely low, checking GPS for closest gas station\n")
        sleep(1.5)
        print("The closest gas station is", gasStations(), "which is", milesToGasStationLow, "miles away.")  # Provide nearby gas station info
    elif gasLevelIndicator == "Quarter Tank":
        print("Your gas tank is on a quarter of a tank, checking GPS for closest gas station\n")
        sleep(1.5)
        print("The closest gas station is", gasStations(), "which is", milesToGasStationQuarterTank, "miles away")  # Provide nearby gas station info
    elif gasLevelIndicator == "Half Tank":
        print("Your gas tank is half full which is plenty enough to get to your destination.")  # Safe gas level message
    elif gasLevelIndicator == "Three Quarter Tank":
        print("Your gas tank is three quarters full.")  # Inform user of good gas level
    else:
        print("Your gas tank is full")  # Inform user that tank is full

# Call the gas level alert function to execute the code
gasLevelAlert()
