print("\n**************************************\n")


print("Gasoline Branch")
import random
from time import sleep

def gasLevelGauge ():
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    return random.choice(gasLevelList)

def gasStations():
    listOfGasStations = ["VP","Shell","Meijer","Sams Club","Marathon","Mobile","Speedway","Circle K"]
    return random.choice(listOfGasStations)

def gasLevelAlert():
    milesToGasStationLow = random.uniform(1,25)
    milesToGasStationQuarterTank = random.uniform(25.1,50)
    gasLevelIndicator = gasLevelGauge()
    if gasLevelIndicator == "Empty":
        print("***WARNING - YOU ARE ON EMPTY***\n")
        sleep(1.5)
        print("Calling Triple AAA")
    elif gasLevelIndicator == "Low":
        print("Your gas tank is extremely low, checking GPS for closest gas station\n")
        sleep(1.5)
        print("The closest gas station is", gasStations(), "which is", milesToGasStationLow,"miles away.")
    elif gasLevelIndicator == "Quarter Tank":
        print("Your gas tank is on a quarter of a tank, checking GPS for closest gas station\n")
        sleep(1.5)
        print("The closest gas station is", gasStations(),"which is",milesToGasStationQuarterTank, "miles away")
    elif gasLevelIndicator == "Half Tank":
        print("Your gas tank is half full which is plenty enough to get to your destination.")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("Your gas tank is three quarters full.")
    else:
        print("Your gas tank is full")
gasLevelAlert()