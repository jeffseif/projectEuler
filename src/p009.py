#! /usr/bin/python3
###
# A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,
#   a^2 + b^2 = c^2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
###
from euler import * ;
###
if __name__ == '__main__':
    top = 1000;
    for a in range(top):
        a2 = a ** 2;
        for b in range(top):
            if b <= a:
                continue;
            b2 = b ** 2
            c = 1000 - a - b;
            if c <= a or c <= b:
                continue;
            if c ** 2 == a2 + b2:
                print(a * b * c);
                break;
