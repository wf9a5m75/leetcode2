class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        prevPrice = 2**31
        for price in prices:
            profit = max(profit - prevPrice + price, profit)
            prevPrice = price
        return profit
