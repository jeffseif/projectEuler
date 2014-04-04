#! /usr/bin/python3
###
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
# The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
###
from euler import * ;
###
if __name__ == '__main__':
    products = [];
    for multiplicand in range(1, 10000):
        minimum = int(exp(log(1e3 * sqrt(10)) - log(multiplicand)));
        maximum = int(exp(log(1e4) - log(multiplicand)));
        for multiplier in range(minimum, maximum):
            digits = '%d%d%d' % (multiplicand, multiplier, multiplicand * multiplier);
            if IsPandigital(digits):
                products.append(multiplicand * multiplier);
    ###
    print(sum(set(products)));
