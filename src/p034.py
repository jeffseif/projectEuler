#! /usr/bin/python
###
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.
###
from euler import * ;
###
if __name__ == '__main__':
    results = set();
    for order in range(3, 9):
        for tens in Combinations(order2Digits[order], order):
            if IsSortedCuriousNumber(tens):
                results.update((sum(digit2Factorial[digit] for digit in tens), ));
    ###
    print(sum(results));
