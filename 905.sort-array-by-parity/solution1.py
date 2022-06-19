#
# Two pointers approach
#  time compelixty: O(N)
#  space complexity: O(N)
#
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even = 0
        for i in range(len(nums)):
            if (nums[i] & 1 == 0):
                nums[even], nums[i] = nums[i], nums[even]
                even += 1
        return nums
