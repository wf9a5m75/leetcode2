class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        size = len(nums)
        L = 0
        R = size - 1
        while(L <= R):
            mid = (L + R) >> 1
            if ((mid + 1 < size) and (nums[mid] <= nums[mid + 1])):
                L = mid + 1
            else:
                R = mid - 1
        return L
