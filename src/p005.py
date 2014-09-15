#! /usr/bin/python3

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

from euler import *

if __name__ == '__main__':
    top = 20

    lcm = 1
    for number in range(2, top + 1):
        lcm = LeastCommonMultipler(lcm, number)

    print(lcm)
