#! /usr/bin/python3
###
# 2 ^ 15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 21000?
###
from euler import *
###
if __name__ == '__main__':
    base = 2
    exponent = 1000
    ###
    print(sum(int(character) for character in str(Power(base, exponent))))
