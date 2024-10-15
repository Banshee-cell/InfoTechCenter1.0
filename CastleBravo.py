print ("\n**********************\n")

print("Weather Branch\n")

#Import Libraries Here
import random
from time import sleep
def weather():
    weatherForecast = ["snowy", "rainy", "blizzard" , "windy" , "icy" , "sunny"]
    weatherCondition=random.choice(weatherForecast)
    return weatherCondition

#print(weather())
weatherAlert = weather()


def vehicleResponseSystem():
    if weatherAlert == "snowy":
        print("\nThe national Weather Service has updated our alarm by 30 minutes because" 
              "of the forecast",weatherAlert, "weather conditions")

        sleep(1)
        print("VRS system has been engaged only allowing you to drive 55mph.")
    elif weatherAlert == "rainy":
        print("\nThe National Weather Service has updated our alarm by 5 minutes because"
              "of the forecast of" ,weatherAlert, "weather conditions")

        sleep(1)

    elif weatherAlert == "blizzard":
        print("\nThe National Weather Service has updated our alarm by 1 hour because"
        "of the forecast of", weatherAlert, "weather conditions")

        sleep(1)


    elif weatherAlert == "windy":
        print("\nThe National Weather Service has updated our alarm by 10 minutes because"
        "of the forecast of", weatherAlert, "weather conditions")

        sleep(1)
    elif weatherAlert == "icy":
        print("\nThe National Weather Service has updated our alarm by 50 minutes because"
        "of the forecast of", weatherAlert, "weather conditions")

    elif weatherAlert == "sunny":
        print("\nThe National Weather Service has turned off because of" ,weatherAlert,"sky's")

vehicleResponseSystem()