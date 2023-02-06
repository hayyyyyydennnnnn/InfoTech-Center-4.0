# Programmer: Hayden Coates
# Date: 1.30.2023
# Program: Infotech Center 4.0 - Gasoline

"""
We will create a Function that will tell us our Fuel Gauge level
    - Create a List with Gas Levels
    - Randomize and choose from the list to determine our gas level

Create a Function to determine our closest Gas Station
    - Create a list of gas stations
    - Randomnly choose a gas station from the list

Create a function to determine our gas level and closest gas station
    - Print gas level
    - Print Closest Gas Station
"""

# Import Libraries Here
import random
from time import sleep


# Gas Level Function
def gasLevelGauge():
    gasLevelList = ["Empty","Low","Quarter Tank","Half Tank","Three Quarter Tank","Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

# Variable calling gasLevelGauge function to store its value
gasLevelIndicator = gasLevelGauge()

#List of Gas Stations Function
def listOfGasStations():
    gasStations = ["Shell","Costco","Buc-ee's","Speedway","7-11","Cricle-K","Meijer","Marathon"]
    gasStationNearBy = random.choice(gasStations)
    return gasStationNearBy

# Determine Gas Level & Closest gas station
def gasLevelAlert():
    milesToGasStaionLow = round(random.uniform(1, 25), 2)
    milesToGasStaionQuarterTank = round(random.uniform(26, 50), 2)
    if gasLevelIndicator == "Empty":
        print("***WARNING YOU ARE ON EMPTY***")
        sleep(1)
        print("Calling Emergency Contact")
    elif gasLevelIndicator == "Low":
        print("****Warning****")
        sleep(1)
        print("Your Gas Tank is very low, checking Google Maps for the closest Gas Station.")
        sleep(1)
        print("The closest gas station is", listOfGasStations(), "whitch is", milesToGasStaionLow,"miles away")
    elif gasLevelIndicator == "Quarter":
        print("***Warning***")
        sleep(1)
        print("Your gas tank is at a Quarter Tank and the closest gas station is", listOfGasStations(), "whitch is", milesToGasStaionQuarterTank,"miles away.")
    elif gasLevelIndicator == "Half Tank":
        print("Your gas tank is half full witch is plenty of gas to make it to your destinations today.")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("Your gas tank is three quarters full witch is plenty of gas to make it to your destinations today.")
    elif gasLevelIndicator == "Full Tank":
        print("Your gas tank is full witch is plenty of gas to make it to your destinations today.")
    else:
        print("your gas tank is Full - Yeah! - Congrats - Vroom Vroom")




gasLevelAlert()













