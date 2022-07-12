class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if (N == 1):
            return nums[0]
        if (N == 2):
            return max(nums)

        return max(self.robbing(nums, 0, N - 2), self.robbing(nums, 1, N - 1))

    def robbing(self, nums: List[int], startIdx: int, endIdx: int) -> int:
        dp = [0] * (endIdx - startIdx + 2)
        dp[0] = nums[startIdx]
        dp[1] = max(dp[0], nums[startIdx + 1])

        for i in range(startIdx + 2, endIdx + 1):
            dp[i - startIdx] = max(dp[i - startIdx - 1], dp[i - startIdx - 2] + nums[i])

        return dp[endIdx - startIdx]
