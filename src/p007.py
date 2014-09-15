#! /usr/bin/python3

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10001st prime number?

from euler import *

if __name__ == '__main__':
    count = 10001

    number = 1
    knownPrimes = []

    while count:
        number += 1
        if IsNotDivisible(number, knownPrimes):
            knownPrimes.append(number)
            count -= 1

    print(number)
