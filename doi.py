# Programmer: Hayden Coates
# Date: 2,15,2023
# Program: Infotech Center 4.0 - Restaurants

"""
We will create a Function that will tell us how far the nearest Restaurants is 
"""

# Import Libraries Here
import random
from time import sleep

# Gas Level Function
def gasLevelGauge():
    gasLevelList = ["Quarter Tank","Half Tank","Three Quarter Tank","Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

# Variable calling gasLevelGauge function to store its value
gasLevelIndicator = gasLevelGauge()
