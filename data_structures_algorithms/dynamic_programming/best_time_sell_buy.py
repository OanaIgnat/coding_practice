"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_buy = float("inf")
        profit = 0
        for i, price in enumerate(prices):
            if price < min_buy:
                min_buy = price
            else:
                profit = max(profit, price - min_buy)
        return profit

    """
    Say you have an array for which the ith element is the price of a given stock on day i.

    Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
    
    Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
    
    Example 1:
    
    Input: [7,1,5,3,6,4]
    Output: 7
    Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
                 Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
    """

    def maxProfit_all(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i - 1] < prices[i]:
                profit += prices[i] - prices[i - 1]

        return profit