class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1
        while(L <= R):
            mid = (L + R) >> 1
            if (nums[mid] == target):
                return mid

            if (nums[L] <= nums[mid]):
                # The left values of the middle are smaller than middle

                if (nums[L] <= target < nums[mid]):
                    R = mid - 1
                else:
                    L = mid + 1
            else:
                # The right values of the middle are greater than middle
                if (nums[mid] < target <= nums[R]):
                    L = mid + 1
                else:
                    R = mid - 1

        if (L < len(nums)) and (nums[L] == target):
            return L
        elif (R >= 0) and (nums[R] == target):
            return R
        else:
            return -1
