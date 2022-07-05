class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 2)
        # dp[n] = 0
        # dp[n + 1] = 0
        for i in range(n - 1, -1, -1):
            dp[i] = min(dp[i + 1], dp[i + 2])  + cost[i]
        return min(dp[0], dp[1])
