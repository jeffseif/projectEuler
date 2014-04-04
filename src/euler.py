#! /usr/bin/python3

###
### Import
###

from math import ceil, exp, floor, log10, log, sqrt;
from itertools import combinations_with_replacement as Combinations;

###
### Functions
###

def MaximumPrimeFactor(number):
    ###
    for divisor in range(2, int(floor(number ** 0.5))):
        if not number % divisor:
            return MaximumPrimeFactor(number // divisor);
    ###
    return number;
###
def IsPalindrome(string):
    return string == string[::-1];
###
def GreatestCommonDenominator(one, two):
    while two:
        one, two = two, one % two;
    ###
    return one;
###
def LeastCommonMultipler(one, two):
    return abs(one) // GreatestCommonDenominator(one, two) * abs(two);
###
def PrimeFactors(big):
    for number in range(2, ceil(big / 2)):
        if not big % number:
            output = [number];
            output.extend(PrimeFactors(big // number));
            return output;
    ###
    return [big];
###
def UniqueFactor(big, little):
    output = 1;
    for number in PrimeFactors(little):
        if number in PrimeFactors(big):
            big /= number;
        else:
            output *= number;
    ###
    return output;
###
def IsNotDivisible(number, knownPrimes):
    for prime in knownPrimes:
        if not number % prime:
            return False;
    ###
    return True;
###
def StringProduct(string):
    output = 1;
    for number in string:
        output *= int(number);
    ###
    return output;
###
def PrimesBelow(limit):
    limit = int(float(limit));
    sieveBound = int((limit - 1) / 2);
    sieve = [True] * sieveBound;
    crossLimit = int(limit ** 0.5 / 2);
    for index in range(crossLimit):
        if sieve[index]:
            for jndex in range(2 * (index + 1) * (index + 2) - 1, sieveBound, 3 + index * 2):
                sieve[jndex] = False;
    ###
    output = [2];
    output.extend(3 + index * 2 for index in range(sieveBound) if sieve[index]);
    return output;
###
def Raw2Matrix(raw):
    return [[int(word) for word in line.strip().split()] for line in raw.split('\n')];
###
def Product(container):
    product = 1;
    for each in container:
        product *= each;
    return product;
###
def Factors(number):
    factors = [];
    for divisor in range(2, int(number ** 0.5) + 1):
        if not number % divisor:
            factors.extend([divisor, number / divisor]);
    ###
    return set(factors);
###
def Raw2List(raw):
    return [int(word) for word in raw.split('\n')];
###
def P14Next(number):
    if number % 2:
        return 1 + 3 * number;
    else:
        return number / 2;
###
def PascalExpand(previousRow):
    output = [1];
    for index in range(1, len(previousRow)):
        output.append(previousRow[index - 1] + previousRow[index]);
    output.append(1);
    ###
    return output;
###
def PascalContract(previousRow):
    return [previousRow[index - 1] + previousRow[index] for index in range(1, len(previousRow))];
###
def Power(base, exponent):
    if not exponent:
        return 1;
    elif exponent < 0:
        return 1 / Power(base, -exponent);
    elif exponent == 1:
        return base;
    elif exponent % 2:
        return base * Power(base, (exponent - 1) / 2) ** 2;
    else:
        return Power(base * base, exponent / 2);
###
def NumberWordPrefix(index, flag = False):
    return [None, None, 'twen', 'thir', ['four', 'for'][flag], 'fif', 'six', 'seven', 'eigh', 'nine'][index];
###
def Number2Words(number):
    if number > 999:
        words = '{} thousand'.format(Number2Words(number // 1000));
        if number % 1000:
            words += ' {}'.format(Number2Words(number % 1000));
        return words;
    if number > 99:
        words = '{} hundred'.format(Number2Words(number // 100));
        if number % 100:
            words += ' and {}'.format(Number2Words(number % 100));
        return words;
    if number > 19:
        words = '{}ty'.format(NumberWordPrefix(number // 10, True));
        if number % 10:
            words += '-{}'.format(Number2Words(number % 10));
        return words;
    if number > 12:
        return '{}teen'.format(NumberWordPrefix(number - 10));
    if number:
        return ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve'][number - 1];
###
def CountLetters(word):
    return len(word.replace(' ', '').replace('-', ''));
###
class Triangle:
    def __init__(self, raw):
        if type(raw) == list:
            self.myRows = raw;
        else:
            self.myRows = [[int(word) for word in row.split(' ') if word.strip()] for row in raw.strip().split('\n')]
        return;
    ###
    def __int__(self):
        return int(self.myRows[0][0]);
    ###
    def __len__(self):
        return len(self.myRows);
    ###
    def CollapseRow(self):
        lastRow = self.myRows.pop();
        lastLastRow = self.myRows.pop();
        self.myRows.append([lastLastRow[index] + max(lastRow[index], lastRow[index + 1]) for index in range(len(lastRow) - 1)]);
        return;
###
def MaximumRouteSum(triangle):
    while len(triangle) > 1:
        triangle.CollapseRow();
    ###
    return int(triangle);
###
def IsASunday(dayNumber):
    return not (dayNumber + 1) % 7
###
def IsNotLeapYear(year):
    if year % 100:
        return year % 4;
    return (year / 100) % 4;
###
def DaysInMonth(month, year):
    if month == 1:
        if IsNotLeapYear(year):
            return 28;
        return 29;
    elif month in [3, 5, 8, 10]:
        return 30;
    else:
        return 31;
###
def DaysInYear(year):
    return 365 + 1 ** (1 - IsNotLeapYear(year));
###
def Factorial(number):
    if number > 1:
        return number * Factorial(number - 1);
    ###
    return 1;
###
def ProperDivisorsSum(number):
    divisors = [1];
    for divisor in range(2, int(number ** 0.5) + 1):
        if not number % divisor:
            divisors.extend([divisor, number // divisor]);
    ###
    return sum(set(divisors));
###
def ReadFile(fileName):
    with open(fileName, 'r') as f:
        ###
        return f.read();
###
def LoadNames(fileName):
    return [word.strip() for word in ReadFile(fileName).split(' ') if word.strip()];
###
def Letter2Score(letter):
    return 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.find(letter) + 1;
###
def ScoreName(name, index):
    score = 0;
    for letter in name:
        score += Letter2Score(letter);
    ###
    return score * index;
###
def IsAbundant(number):
    return ProperDivisorsSum(number) > number;
###
def SwapReverse(string, index, jndex):
    characters = [character for character in string];
    characters[index], characters[jndex] = characters[jndex], characters[index]
    return ''.join(characters[ : index + 1]) + ''.join(characters[ : index : -1]);
###
def Permute(string):
    jndex = False;
    if string:
        for index in range(len(string) - 1):
            index = len(string) - index - 2;
            if string[index] < string[index + 1]:
                jndex = True;
                break;
    if jndex:
        for jndex in range(len(string) - 1):
            jndex = len(string) - jndex - 1;
            if string[index] < string[jndex]:
                return SwapReverse(string, index, jndex);
###
def LongDivision(divisor, dividend = 1):
    dividends = [];
    while dividend:
        while not dividend // divisor:
            dividend *= 10;
        if dividend not in dividends:
            dividends.append(dividend);
            dividend %= divisor;
        else:
            return dividends;
    ###
    return [];
###
def SumPowerOfDigits(number, digit2Power):
    return sum(digit2Power[digit] for digit in str(number));
###
def WaysToChange(target, index, coins):
    if index < 1:
        return 1;
    ###
    return sum(WaysToChange(target - coins[index] * jndex, index - 1, coins) for jndex in range(target // coins[index] + 1));
###
def IsPandigital(multiplicand, multiplier):
    return set(int(number) for number in '%d%d%d' % (multiplicand, multiplier, multiplicand * multiplier)) == panDigits;
###
def IsCuriousFraction(dividend, divisor):
    if divisor % 10:
        for index in range(len(str(dividend))):
            for jndex in range(len(str(divisor))):
                if str(dividend)[index] == str(divisor)[jndex] and dividend * int(str(divisor)[1 - jndex]) == divisor * int(str(dividend)[1 - index]):
                    return True;
    return False;
###
def GetOrder(number):
    return int(log10(number + 1e-1)) + 1
###
def IsSortedCuriousNumber(tens):
    return sorted(str(sum(digit2Factorial[digit] for digit in tens))) == sorted(str(n) for n in tens);
###
def OnlyOdds(number):
    return all(c in '13579' for c in number);
###
def IsTruncatable(prime, primes):
    ###
    # Left
    ###
    temp = prime;
    while temp >= 10:
        temp /= 10;
        if temp not in primes:
            return False;
    ###
    # Right
    ###
    temp = prime;
    while temp >= 10:
        temp %= 10 ** int(log10(temp));
        if temp not in primes:
            return False;
    ###
    return True;

###
### Constants
###

digit2Factorial = {digit : Factorial(digit) for digit in range(10)};
order2Digits = {tens : sorted(digit for digit, factorial in digit2Factorial.items() if tens >= GetOrder(factorial)) for tens in range(10)};
panDigits = set(range(1, 10));
