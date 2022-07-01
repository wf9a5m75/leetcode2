class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums)
        while(L < R):
            mid = (L + R) >> 1
            if (nums[mid] < target):
                L = mid + 1
            else:
                R = mid
        return L if (0 <= L < len(nums)) and (nums[L] == target) else -1
