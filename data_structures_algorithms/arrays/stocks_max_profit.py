from typing import List
'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        min_price = float('+inf')
        for i, price_i in enumerate(prices):
            if price_i < min_price:
                min_price = price_i
            else:
                max_profit = max(price_i - min_price, max_profit)
        return max_profit