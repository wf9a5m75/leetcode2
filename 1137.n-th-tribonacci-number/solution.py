class Solution:
    def tribonacci(self, n: int) -> int:
        if (n < 3):
            return 0 if n == 0 else 1
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 1
        for i in range(n - 2):
            dp[i + 3] = dp[i] + dp[i + 1] + dp[i + 2]
        return dp[n]
