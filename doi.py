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


# Gas Level Function
def gasLevelGauge():
    gasLevelList = ["Empty","Low","Quarter Tank","Half Tank","Three Quarter Tank","Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

print(gasLevelGauge())

def listOfGasStations():
    gasStations = ["Shell","Costco","buccee","Speedway","7-11","Cricle-K","Meijer","Marathon"]
    gasStationNearBy = random.choice(gasStations)
    print(gasStationNearBy)
    return gasStationNearBy




