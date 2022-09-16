class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        size = len(nums)
        if (size > 1) and ((nums[0] > nums[1])):
            return 0
        if (size > 1) and (nums[size - 2] < nums[size - 1]):
            return size - 1

        L = 0
        R = size - 1
        while(L < R):
            mid = (L + R) >> 1
            if (nums[mid] < nums[mid + 1]):
                L = mid + 1
            else:
                R = mid
        return L
        
