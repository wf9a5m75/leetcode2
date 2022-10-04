class Solution:
    def rob(self, nums: List[int]) -> int:

        N = len(nums)
        if (N == 1):
            return nums[0]

        dp = [[0] * (N + 2) for _ in range(2)]

        def robbering(dpIdx: int, i: int, end: int) -> int:

            for j in range(i, end):
                dp[dpIdx][j + 1] = max(dp[dpIdx][j + 1], dp[dpIdx][j])
                dp[dpIdx][j + 2] = dp[dpIdx][j] + nums[j]

            return max(dp[dpIdx][end], dp[dpIdx][end + 1])
        return max(robbering(0, 0, N - 1), robbering(1, 1, N))
