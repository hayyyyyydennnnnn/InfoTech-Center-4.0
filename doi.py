
#Programmer: Hayden Coates
#Date: 1/24/23
#Program: InfoTech 4.0

"""
Our Welcome Screen will start our program letting
drivers know that the InfoTech Center 4.0 OS is loading
"""

#Import Libraries Here
import time
import sys  # I imported the system library for further use in code.

timeToSleep = 2
print("\n\n\033[1;33;40mWelcome - InfotechCenter 4.0\n")
time.sleep(timeToSleep)

#print("\nInfotech Center 4.0 OS is loading")
x = 0
a = 0

while x != 20:
    x += 1
    b = ("\033[1;33;40mInfotech Center 4.0 OS is loading" + "." * a)
    sys.stdout.write('\r' + b)  # \r prints a carriage return first, so `b` is printed on top of the previous line.
    time.sleep(0.5)
    if a == 4:
        a = 0
    if x == 20:
        print('\n\n\033[1;32;40mMission Accomplished')

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














