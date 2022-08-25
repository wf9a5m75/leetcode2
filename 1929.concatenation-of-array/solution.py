class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        size = len(nums)
        for i in range(size):
            nums.append(nums[i])
        return nums
