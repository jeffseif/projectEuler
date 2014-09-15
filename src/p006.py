#! /usr/bin/python3

# The sum of the squares of the first ten natural numbers is,
#   12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
#   (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
#   3025 - 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum

from euler import *

if __name__ == '__main__':
    top = 100

    print(sum((index + 1) * (jndex + 1) for index in range(top) for jndex in range(top) if index != jndex))
