# sort approach
#
#   time complexity: O(N log N)
#   space complexity: O(1)
#
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        # O(N)
        for i in range(len(nums)):
            nums[i] = nums[i] ** 2

        # O(N log N)
        nums.sort()
        return nums
