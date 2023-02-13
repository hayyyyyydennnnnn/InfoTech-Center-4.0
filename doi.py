# programmer: Hayden Coates 
# date: 2,9,23
# program: Weather System Updates

#Import Libraries here 
import random

#Create weather condtion in a list and choose it randomly
def weather():
    weatherForcast = ["Snowing","Blizzard","Rain","Foggy","Windy","Icy","Sunshine"]
    weatherCondition = random.choice(weatherForcast)
    return weatherCondition

# Variable to call weather() once in our VRS 
weatherAlert = weather() 


print(weatherAlert)

# VRS() to respond to the weather condotion
def vehicleResponseSystem():
    if weatherAlert == "Snowing":
        print("\nNWS has changed your alarm by 15 minutes because of the weather of",weatherAlert)
        print("your VRS has been engaged only alowing your vehicle to go 45 in MPH")
    elif weatherAlert == "Blizzard":
        print("\nNWS has changed your alarm by 30 minutes because of the weather of",weatherAlert)
        print("your VRS has been engaged only alowing your vehicle to go 30 in MPH")
    elif weatherAlert == "Rain":
        print("\nNWS has not changed your alarm",weatherAlert,", please go the speed limit and be careful")
    elif weatherAlert == "Foggy":
        print("\nNWS has not changed your alarm",weatherAlert,", please go the speed limit and be careful")
    elif weatherAlert == "Windy":
        print("\nNWS has not changed your alarm",weatherAlert,", please go the speed limit and be extra careful")
    elif weatherAlert == "Blizzard":
        print("\nNWS has changed your alarm by 60 minutes because of the weather of",weatherAlert)
        print("your VRS has been engaged only alowing your vehicle to go 25 in MPH")
    else:
        print("\nNWS has not changed your alarm",weatherAlert,", please go the speed limit")



vehicleResponseSystem()