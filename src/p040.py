#! /usr/bin/python
###
# An irrational decimal fraction is created by concatenating the positive integers:
#   0.123456789101112131415161718192021...
# It can be seen that the 12th digit of the fractional part is 1.
# If dn represents the nth digit of the fractional part, find the value of the following expression.
#   d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000
###
from euler import *
###
if __name__ == '__main__':
    digits = (1, 1, 5, 3, 7, 2, 1)
    print(reduce(lambda n, m: n * m, digits))
