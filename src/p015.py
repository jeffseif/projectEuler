#! /usr/bin/python3

# Starting in the top left corner of a 22 grid, there are 6 routes (without backtracking) to the bottom right corner.
# How many routes are there through a 2020 grid?

from euler import *

if __name__ == '__main__':
    gridDimension = 20

    row = [1]
    while len(row) <= gridDimension:
        row = PascalExpand(row)
    while len(row) > 1:
        row = PascalContract(row)

    print(row[0])
