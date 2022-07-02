class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums)
        while(L < R):
            mid = (L + R) >> 1
            if (nums[mid] == target):
                return mid
            elif (nums[mid] < target):
                L = mid + 1
            else:
                R = mid
        # if (L < 0):
        #     return 0
        return L
