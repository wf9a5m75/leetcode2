class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        # O(N)
        for i in range(len(nums)):
            nums[i] = nums[i] ** 2

        # O(N log N)
        nums.sort()
        return nums
