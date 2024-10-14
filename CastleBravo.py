print ("\n**********************\n")

print("Weather Branch\n")

#Import Libraries Here
import random
from time import sleep
def weather():
    weatherForecast = ["snowy", "blizzard", "rainy" , "windy" , "icy" , "sunny"]
    weatherCondition=random.choice(weatherForecast)
    return weatherCondition

#print(weather())
weatherAlert = weather()


def vehicleResponseSystem():
    if weatherAlert == "snowy":
         print("\nThe national Weather Service has updated our alarm by 30 minutes because"
         " of the forcast of", weatherAlert, "weather condition.")

vehicleResponseSystem()