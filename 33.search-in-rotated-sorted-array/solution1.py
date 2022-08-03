from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        size = len(nums)
        if (size == 1):
            return 0 if nums[0] == target else -1

        L = 0
        R = size - 1

        while(L <= R):
            mid = (L + R) >> 1

            if (nums[mid] == target):
                # target = 3
                # nums = [1, 2, 3, 4, 0]
                #         L     M     R
                return mid
            elif (nums[L] <= nums[mid]):
                if (nums[L] <= target < nums[mid]):
                    # target = 3
                    # nums = [2, 3, 4, 0, 1]
                    #         L     M     R
                    R = mid - 1
                else:
                    # target = 3
                    # nums = [0, 1, 2, 3, 4]
                    #         L     M     R
                    L = mid + 1
            else:
                if (nums[mid] < target <= nums[R]):
                    # target = 3
                    # nums = [4, 0, 1, 2, 3]
                    #         L     M     R
                    L = mid + 1
                else:
                    R = mid - 1

        return L if (0 <= L < size) and (nums[L] == target) else -1
print(Solution().search([0,1,2,3,4], 3) == 3)
print(Solution().search([4,0,1,2,3], 3) == 4)
print(Solution().search([3,4,0,1,2], 3) == 0)
print(Solution().search([2,3,4,0,1], 3) == 1)
print(Solution().search([1,2,3,4,0], 3) == 2)
print(Solution().search([4,5,6,7,0,1,2], 4) == 0)
print(Solution().search([4,5,6,7,0,1,2], 3) == -1)
print(Solution().search([1], 0) == -1)
print(Solution().search([1,3,5], 3) == 1)
print(Solution().search([1,3], 4) == -1)
print(Solution().search([1], 2) == -1)
print(Solution().search([3,1], 1) == 1)
print(Solution().search([1,3], 1) == 0)
