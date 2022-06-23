#
# Greedy approach
#
#  Time complexity : O(N)
#  Space complexity: O(1)
#
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        lowest = 10000
        profit =  0
        for price in prices:
            lowest = min(lowest, price)
            profit = max(profit, price - lowest)
        return profit
