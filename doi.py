# programmer: Hayden Coates 
# date: 2,9,23
# program: Weather System Updates

#Import Libraries here 
import random

#Create weather condtion in a list and choose it randomly
def weather():
    weatherForcast = ["Snowing","Blizards","Raining","Foggy","Windy","Icy","Sunshine"]
    weatherCondition = random.choice(weatherForcast)
    return weatherCondition

# Variable to call weather() once in our VRS 
weatherAlert = weather() 

print(weatherAlert)

# VRS() to respond to the weather condotion
def vehicleResponseSystem():
    print("Howdy")