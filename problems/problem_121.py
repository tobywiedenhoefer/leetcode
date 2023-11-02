# LINK: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a
# different day in the future to sell that stock
# Return the maximum profit you can achieve from this transaction.
# If you cannot achieve any profit, return 0.

import typing


def max_profit(prices: typing.List[int]):
    profit = 0
    a, b = 0, 1
    while b <= (len(prices) - 1):
        if prices[b] < prices[a]:
            a = b
        profit = max(profit, prices[b] - prices[a])
        b += 1
    return profit
