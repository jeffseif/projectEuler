#! /usr/bin/python
###
# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# How many circular primes are there below one million?
###
from euler import *
###
if __name__ == '__main__':
    limit = 1e6
    primesBelow = [str(prime) for prime in PrimesBelow(limit)]
    onlyOdds = [prime for prime in primesBelow if OnlyOdds(prime)]
    onlyOdds.append('2')
    ###
    circularPrimes = 0
    for prime in reversed(onlyOdds):
        match = True
        for index in range(len(prime)):
            if prime[index : ] + prime[ : index] not in onlyOdds:
                match = False
                break
        ###
        circularPrimes += match
    ###
    print(circularPrimes)
