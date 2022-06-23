#
# DP approach
#
#  Time complexity : O(N)
#  Space complexity: O(N)
#
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        N = len(prices)

        # dp[0] = buy
        # dp[1] = sell
        dp = [ [0] * N for _ in range(2) ]

        dp[0][0] = -prices[0]
        for idx in range(1, N):
            price = prices[idx]

            # buy
            dp[0][idx] = max(dp[0][idx - 1], -price)

            # sell
            dp[1][idx] = max(dp[1][idx - 1], dp[0][idx - 1] + price)

        return dp[1][N - 1]
