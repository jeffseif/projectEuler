#! /usr/bin/python
###
# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
# (Please note that the palindromic number, in either base, may not include leading zeros.)
###
from euler import * ;
###
if __name__ == '__main__':
    limit = 1e6;
    decimalPalindromes = [number for number in range(1, int(limit) + 1) if IsPalindrome(str(number))];
    bothPalindromes = [number for number in decimalPalindromes if IsPalindrome(bin(number)[2 : ])];
    ###
    print(sum(bothPalindromes));
