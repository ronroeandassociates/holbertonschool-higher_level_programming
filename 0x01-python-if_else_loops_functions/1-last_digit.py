#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
modnum = number % 10 if number > 0 else number % -10
if modnum > 5:
    print(f"Last digit of {number} is {modnum} and is greater than 5")
elif modnum == 0:
    print(f"Last digit of {number} is {modnum} and is 0")
else:
    print(f"Last digit of {number} is {modnum} and is less than 6 and not 0")
