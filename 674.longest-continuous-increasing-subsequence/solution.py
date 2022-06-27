class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        result = 0
        cnt = 0
        prev = nums[0] - 1
        for num in nums:
            cnt = cnt + 1 if prev < num else 1
            prev = num
            result = max(result, cnt)
        return result
