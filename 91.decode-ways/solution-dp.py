class Solution:
    def numDecodings(self, s: str) -> int:
        size = len(s)

        if (s[0] == "0"):
            return 0

        dp = [0] * (size + 1)
        dp[size] = 1
        for i in range(size - 1, -1, -1):
            if (s[i] == "0"):
                continue

            if (i + 1 <= size):
                dp[i] += dp[i + 1]

            if (i + 2 <= size) and (int(s[i:i+2]) <= 26):
                dp[i] += dp[i + 2]

        return dp[0]
