#! /usr/bin/python3

# You are given the following information, but you may prefer to do some research for yourself.
#   1 Jan 1900 was a Monday.
#   Thirty days has September,
#   April, June and November.
#   All the rest have thirty-one,
#   Saving February alone,
#   Which has twenty-eight, rain or shine.
#   And on leap years, twenty-nine.
#   A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

from euler import *

if __name__ == '__main__':
    century = 20

    dayNumber = DaysInYear(100 * (century - 1))
    count = 0
    for year in range(100 * (century - 1) + 1, 100 * century + 1):
        for month in range(12):
            if IsASunday(dayNumber):
                count += 1
            dayNumber += DaysInMonth(month, year)

    print(count)
