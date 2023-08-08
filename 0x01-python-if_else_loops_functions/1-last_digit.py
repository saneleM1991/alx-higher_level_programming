#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lst_digit = 0
if number < 0:
    lst_digit = -(abs(number) % 10)
    if lst_digit < 6 and lst_digit != 0:
        print(f"Last digit of {number} is {lst_digit}and is less than 6 and not 0"
              )
