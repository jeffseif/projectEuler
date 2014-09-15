#! /usr/bin/python3

# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
#   21 22 23 24 25
#   20  7  8  9 10
#   19  6  1  2 11
#   18  5  4  3 12
#   17 16 15 14 13
# It can be verified that the sum of the numbers on the diagonals is 101.
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

from euler import *

if __name__ == '__main__':
    side = 1001

    rows = side // 2
    total = 1
    corner = 1
    for row in range(rows):
        total += 4 * corner + 10 * 2 * (row + 1)
        corner += 8 * (row + 1)

    print(total)
