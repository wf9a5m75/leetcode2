class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        result = partialMax = -10**4 - 1
        for num in nums:
            partialMax = max(partialMax + num, num)
            result = max(result, partialMax)
        return result
