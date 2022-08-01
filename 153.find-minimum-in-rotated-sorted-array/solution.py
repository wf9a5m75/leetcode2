class Solution:
    def findMin(self, nums: List[int]) -> int:
        if (nums[0] <= nums[-1]):
            return nums[0]

        L = 0
        R = len(nums) - 1
        while(L <= R):
            mid = (L + R) >> 1

            if (nums[mid - 1] < nums[mid]):
                if (nums[0] > nums[mid]):
                    R = mid - 1
                else:
                    L = mid + 1
            else:
                return nums[mid]
        return nums[L]
