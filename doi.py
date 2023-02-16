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


#List of Restaurants Function
def listOfRestaurants():
    Restaurants = ["Olive Garden","Red Robin","Texas RoadHouse","Panera","Panda Express","Red Lobster","Cheese Cake Factory","The Mealting-Pot"]
    RestaurantsNearBy = random.choice(Restaurants)
    return RestuarantsNearBy

    #List of Fast Food Restaurants Function
def listOfFastFoodRestaurants():
    Restaurants = ["Mc-Donalds","Subway","Taco-Bell","Little Chessers","Culver's","BurgerKing","Wendys","KFC"]
    FastFoodRestaurantsNearBy = random.choice(FastFoodRestaurants)
    return FastFoodRestuarantsNearBy
