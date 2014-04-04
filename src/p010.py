#! /usr/bin/python3
###
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
###
from euler import * ;
###
if __name__ == '__main__':
    limit = 2e6;
    ###
    print(sum(PrimesBelow(limit)));
