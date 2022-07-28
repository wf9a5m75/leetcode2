# Binary Search
#
# nums = [1, 3, 4, 2, 2]
#
# if all numbers appear exactly once,
# the numbers equal or less are the same with the value
#
# 1 ... 1
# 2 ... 1, 2
# 3 ... 1, 2, 3
# 4 ... 1, 2, 3, 4
# 5 ... 1, 2, 3, 4, 5
#
# but if there is a duplicated number, it exceeds the number of elements
#
# nums = [1, 3, 4, 2, 2]
# 1 ... 1
# 2 ... 1, 2, 2 ⇐ duplicated value
# 3 ... 1, 2, 2, 3
# 4 ... 1, 2, 2, 3, 4
#
# ---------
# time complexity : O(n log n)
# space complexity : O(1)
#

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        low = 1
        high = len(nums) - 1

        duplicate = -1
        while(low <= high):
            mid = (low + high) >> 1

            count = 0
            for num in nums:
                count += 1 if num <= mid else 0

            if count > mid:
                duplicate = mid
                high = mid - 1
            else:
                low = mid + 1
        return duplicate
