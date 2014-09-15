#! /usr/bin/python3

# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

from euler import *

if __name__ == '__main__':
    fractions = []

    for dividend in range(int(1e1), int(1e2)):
        for divisor in range(int(dividend + 1), int(1e2)):
            if IsCuriousFraction(dividend, divisor):
                fractions.append((dividend, divisor))

    numerator, denominator = 1, 1
    for (dividend, divisor) in fractions:
        numerator *= dividend
        denominator *= divisor

    bothPrimeFactors = list(set(PrimeFactors(numerator)) & set(PrimeFactors(denominator)))
    while bothPrimeFactors:
        numerator //= bothPrimeFactors[0]
        denominator //= bothPrimeFactors[0]
        bothPrimeFactors = list(set(PrimeFactors(numerator)) & set(PrimeFactors(denominator)))

    print(denominator)
