#!/usr/bin/python3
"""
Defines a function makeChange
"""


def makeChange(coins, total):
    """
    Returns the fewest number of coins needed to meet
    total. If total is 0 or less returns 0 and if total
    cannot be met by any numbers of coins you have returns -1
    """
    if total <= 0:
        return 0
    number_of_coins = 0
    pos = 0  # position in the coin's list
    coins.sort(reverse=True)
    while total > 0:
        if total > 0 and pos > len(coins) - 1:
            return -1
        elif total >= coins[pos]:
            total -= coins[pos]
            number_of_coins += 1
        else:
            pos += 1
    return number_of_coins
