#! /usr/bin/python3
###
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91  99.
# Find the largest palindrome made from the product of two 3-digit numbers.
###
from euler import *
###
if __name__ == '__main__':
    palindromes = []
    for index in range(100, 1000):
        for jndex in range(index, 1000):
            product = index * jndex
            if IsPalindrome(str(product)):
                if product not in palindromes:
                    palindromes.append(product)
    ###
    print(max(palindromes))
