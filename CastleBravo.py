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