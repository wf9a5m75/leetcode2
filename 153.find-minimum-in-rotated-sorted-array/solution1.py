from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        size = len(nums)
        if (size == 1):
            return nums[0]
        if (size == 2):
            return min(nums)

        L = 0
        R = len(nums) - 1
        while(L < R):
            mid = (L + R) >> 1
            if (nums[L] < nums[R]):
                # nums = [0, 1, 2, 3, 4, 5]
                #         L     M        R
                R = mid - 1
            else:
                if (nums[mid] < nums[R]):
                    # nums = [4, 5, 0, 1, 2, 3]
                    #         L     M        R
                    # nums = [5, 0, 1, 2, 3, 4]
                    #         L     M        R
                    # nums = [2, 3, 4, 5, 0, 1]
                    #         L     M        R
                    R = mid
                else:
                    # nums = [3, 4, 5, 0, 1, 2]
                    #         L     M        R
                    L = mid + 1

        return min(nums[L], nums[R])
print(Solution().findMin([0,1,2,3,4]) == 0)
print(Solution().findMin([4,0,1,2,3]) == 0)
print(Solution().findMin([3,4,0,1,2]) == 0)
print(Solution().findMin([2,3,4,0,1]) == 0)
print(Solution().findMin([1,2,3,4,0]) == 0)
print(Solution().findMin([1,2,3]) == 1)
print(Solution().findMin([3,1,2]) == 1)
print(Solution().findMin([2,3,1]) == 1)
print(Solution().findMin([1,2]) == 1)
print(Solution().findMin([2,1]) == 1)
