#! /usr/bin/python3

# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
#   {20,48,52}, {24,45,51}, {30,40,50}
#For which value of p <= 1000, is the number of solutions maximised?

from euler import *

if __name__ == '__main__':
    pythagoreanTriples = ((3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (9, 40, 41), (11, 60,  61), (12, 35,  37), (13, 84,  85), (15, 112, 113), (16, 63,  65), (17, 144, 145), (19, 180, 181), (20, 21,  29), (20, 99,  101), (21, 220, 221), (24, 143, 145), (28, 45,  53), (28, 195, 197), (32, 255, 257), (33, 56,  65), (36, 77,  85), (39, 80,  89), (44, 117, 125), (48, 55,  73), (51, 140, 149), (52, 165, 173), (57, 176, 185), (60, 91,  109), (60, 221, 229), (65, 72,  97), (84, 187, 205), (85, 132, 157), (88, 105, 137), (95, 168, 193), (96, 247, 265), (104, 153, 185), (105, 208, 233), (115, 252, 277), (119, 120, 169), (120, 209, 241), (133, 156, 205), (140, 171, 221), (160, 231, 281), (161, 240, 289), (204, 253, 325), (207, 224, 305))

    factors = set(sum(triple) for triple in pythagoreanTriples)

    solutions, number = max((sum(number // factor for factor in factors if not(number % factor)), number) for number in range(1001))

    print(number)
