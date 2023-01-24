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

print("\n\nWelcome - InfotechCenter 4.0")
time.sleep(timeToSleep)
print("\nInfotech Center 4.0 OS is loading")

#print("\nInfotech Center 4.0 OS is loading")
x = 0
a = 0

while x != 20:
    x += 1
    b = ("\033[1;33;40m Infotech Center 4.0 OS is loading" + "." * a)
    sys.stdout.write('\r' + b)  # \r prints a carriage return first, so `b` is printed on top of the previous line.
    time.sleep(0.5)
    if a == 4:
        a = 0
    if x == 20:
        print('\033[1;32;40m Done!')

