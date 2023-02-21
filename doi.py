# Programmer: Hayden Coates
# Date: 2,15,2023
# Program: Infotech Center 4.0 - Restaurants

"""
We will create a Function that will tell us how far the nearest Restaurants is 
"""

#import Libeares Here
import random
from time import sleep



#List of Restaurants Function
def listOfRestaurants():
    global restaurantNearBy
    Restaurants = ["Olive Garden","Red Robin","Texas RoadHouse","Panera","Panda Express","Red Lobster","Cheese Cake Factory","The Mealting-Pot","Mc-Donalds", "Subway", "Taco-Bell", "Little Chessers", "Culver's", "BurgerKing", "Wendys", "KFC","Chic-Fil-A"]
    restaurantsNearBy = random.choice(Restaurants)
    return restaurantsNearBy



def restaurantDistance():
    milesToRestaurant = round(random.uniform(5, 30), 2)
    restaurant_choice = input("What Restaurant do you want to go to. <")
    if restaurant_choice == "Olive Garden":
        print("The closest Olive Garden is", milesToRestaurant,"miles away")
    elif restaurant_choice == "Red Robin":
        print("The closest Red Robin is", milesToRestaurant,"miles away")
    elif restaurant_choice == "Texas RoadHouse":
        print("The Closest Texas RoadHouse is",milesToRestaurant,"miles away.")
    elif restaurant_choice == "Panera":
        print("The Closest Panera is",milesToRestaurant,"miles away.")
    elif restaurant_choice == "Panda Express":
        print("The closest Panda Express is", milesToRestaurant,"miles away")
    elif restaurant_choice == "Red Lobster":
        print("The closest Red Lobster is", milesToRestaurant,"miles away")
    elif restaurant_choice == "Cheese Cake Factory":
        print("The closest Cheese Cake Factory is", milesToRestaurant, "miles away")
    elif restaurant_choice == "The Mealting-Pot":
        print("The closest The Mealting-Pot is", milesToRestaurant, "miles away")
    elif restaurant_choice == "Mc-Donalds":
        print("The closest Mc-Donalds is", milesToRestaurant, "miles away")
    elif restaurant_choice == "Subway":
        print("The closest Subway is", milesToRestaurant, "miles away")
    elif restaurant_choice == "Taco-Bell":
        print("The closest Taco-Bell is", milesToRestaurant, "miles away")
    elif restaurant_choice == "Little Chessers":
        print("The closest Little Chessers is", milesToRestaurant, "miles away")
    elif restaurant_choice == "Culver's":
        print("The closest Culver's is", milesToRestaurant, "miles away")
    elif restaurant_choice == "BurgerKing":
        print("The closest BurgerKing is", milesToRestaurant, "miles away")
    elif restaurant_choice == "Wendys":
        print("The closest Wendys is", milesToRestaurant, "miles away")
    elif restaurant_choice == "KFC":
        print("The closest KFC is", milesToRestaurant, "miles away")
    elif restaurant_choice == "Chic-Fil-A":
        print("The closest Chic-Fil-A is", milesToRestaurant, "miles away")


restaurantDistance()


