class Solution:
    """
    def lengthOfLIS_TLE(self, nums: List[int]) -> int:
        size = len(nums)

        @cache
        def backtrack(i: int, prevVal: int)-> int:
            if (i == size):
                return 0

            result = backtrack(i + 1, prevVal)
            if (nums[i] > prevVal):
                result = max(result, backtrack(i + 1, nums[i]) + 1)
            return result
        return backtrack(0, -1000000)
    """

    def lengthOfLIS(self, nums: List[int]) -> int:

        size = len(nums)
        dp = [1] * size
        for i in range(size):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
