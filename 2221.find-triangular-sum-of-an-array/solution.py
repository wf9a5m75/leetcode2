class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        size = len(nums)
        if (size == 1):
            return nums[0]

        dp = [0] * (size - 1)
        prev = nums[0]
        for i in range(1,size):
            dp[i - 1] = (prev + nums[i]) % 10
            prev = nums[i]
        return self.triangularSum(dp)
