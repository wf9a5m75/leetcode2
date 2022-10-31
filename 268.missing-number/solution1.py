class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        N = len(nums)
        result = 0
        for i in range(N):
            result = result ^ i ^ nums[i]
        return result ^ N
