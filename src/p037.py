#! /usr/bin/python
###
# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
###
from euler import *
###
if __name__ == '__main__':
    primes = PrimesBelow(8e5)
    ###
    # Remove terminal 1's and 9's
    # Remove beginning 1's and 9's
    ###
    maybeTruncatable = [prime for prime in primes if prime % 10 not in (1, 9)]
    maybeTruncatable = [prime for prime in maybeTruncatable if str(prime)[0] not in ('1', '9')]
    ###
    truncatables = []
    for prime in maybeTruncatable:
        if IsTruncatable(prime, primes):
            truncatables.append(prime)
        ###
        if len(truncatables) > 11 + 3:
            break
    ###
    print(sum(prime for prime in truncatables if prime > 9))
