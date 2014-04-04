#! /usr/bin/python3
###
# n! means n  (n  1)  ...  3  2  1
# Find the sum of the digits in the number 100!
###
from euler import * ;
###
if __name__ == '__main__':
    number = 100;
    ###
    print(sum([int(letter) for letter in str(Factorial(number))]));
