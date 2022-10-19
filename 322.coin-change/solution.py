class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if (amount == 0):
            return 0

        INF = float('inf');
        dp = [INF] * (amount + 1)
        dp[0] = 0

        for coin in coins:

            for price in range(amount):
                if (coin + price <= amount):
                    dp[coin + price] = min(dp[coin + price], dp[price] + 1)

        return -1 if (dp[amount] == INF) else dp[amount]
