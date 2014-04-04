#! /usr/bin/python3
###
# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
#   012   021   102   120   201   210
#   0123  0132  0213  0231  0312  0321  1023  1032  1203  1230  1302  1320  2013  2031  2103  2130  2301  2310  3012  3021  3102  3120  3201  3210
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
###
from euler import * ;
###
if __name__ == '__main__':
    top = 9;
    big = 1e6;
    ###
    string = ''.join(str(number) for number in range(top + 1));
    count = 1;
    while count < big and string:
        string = Permute(string);
        count += 1;
    ###
    print(string);
