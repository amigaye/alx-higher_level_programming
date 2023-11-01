#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    lastDigit = number % 10
else:
    positiveNumber = (-1 * number) % 10
    lastDigit = positiveNumber * -1
print("Last digit of {:d} is ".format(number), end="")
if lastDigit > 5:
    print("is {:d} and is greater than 5".format(lastDigit))
elif lastDigit == 0:
    print("is {:d} and is 0".format(lastDigit))
else:
    print("is {:d} and is less than 6 and not 0".format(lastDigit))
