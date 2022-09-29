class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        size = len(nums)
        if (size == 1):
            return nums[0]

        minP = nums[0]
        maxP = nums[0]
        result = nums[0]
        i = 1
        while(i < size):
            if nums[i] < 0:
                minP, maxP = maxP, minP
            minP = min(nums[i], minP * nums[i])
            maxP = max(nums[i], maxP * nums[i])
            result = max(result, maxP)
            i += 1

        return result
