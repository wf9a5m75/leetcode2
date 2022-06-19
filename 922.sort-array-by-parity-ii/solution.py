#
# Two pointers approach
#  time compelixty: O(N)
#  space complexity: O(N)
#
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        ptrEven = 0
        ptrOdd = 1
        size = len(nums)
        for i in range(size):
            val = nums[i] & 0xFFF

            if (val & 1 == 0):
                nums[ptrEven] = nums[ptrEven] | (val << 12)
                ptrEven += 2
            else:
                nums[ptrOdd] = nums[ptrOdd] | (val << 12)
                ptrOdd += 2

        for i in range(size):
            nums[i] = nums[i] >> 12
        return nums
