# https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14436/Revised-Binary-Search

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1
        while(L < R):
            mid = (L + R) >> 1
            if (nums[mid] == target):
                return mid

            if (nums[L] <= nums[mid]):
                #
                #  [2, 3, 4, 5,  9, 10, 11]
                #   L        mid         R
                #
                #  target = 4
                #
                if (target >= nums[L]) and (target < nums[mid]):
                    R = mid - 1
                else:
                    L = mid + 1
            else:
                #
                #  [9, 10, 11, 2,  3, 4, 5]
                #   L          mid       R
                #
                #  target = 4
                #
                if (target > nums[mid]) and (target <= nums[R]):
                    L = mid + 1
                else:
                    R = mid - 1
        return L if nums[L] == target else -1
