#
# Negative marking
#
# [1, 3, 4, 2, 2]
#
# ------
#    [1,  3, 4, 2, 2]
# num = 1
#         ⇓
#    [1, -3, 4, 2, 2]
# num = 3
#               ⇓
#    [1, -3, 4, -2, 2]
# num = 4
#                    ⇓
#    [1, -3, 4, -2, -2]
# num = 2
#             ⇓
#    [1, -3, -4, -2, -2]
# num = 2
#             ⇓
#    [1, -3, <-4>, -2, -2]
#
# Since nums[2] is negetive value, we visited once.
# Thus the 2 is the duplicated value
#
# ------------
#    time complexity: O(N)
#    space complexity: O(1)



class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # Since all values ranged in 1...n,
        # we can treat the value as index.
        duplicate = -1
        for num in nums:
            idx = abs(num)
            if (nums[idx] < 0):
                duplicate = idx
                break
            nums[idx] *= -1

        # restore numbers
        for i in range(len(nums)):
            nums[i] = abs(nums[i])

        return duplicate
