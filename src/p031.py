#! /usr/bin/python3
# -*- coding: iso-8859-1 -*-
###
# In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
#   1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
# It is possible to make £2 in the following way:
#   1£1 + 150p + 220p + 15p + 12p + 31p
# How many different ways can £2 be made using any number of coins?
###
from euler import * ;
###
if __name__ == '__main__':
    coins = (1, 2, 5, 10, 20, 50, 100, 200);
    ###
    print(WaysToChange(max(coins), len(coins) - 1, coins));
