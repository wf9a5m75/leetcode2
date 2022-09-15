class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        size = len(nums)
        if (size == 0) or (target < nums[0]) or (nums[-1] < target):
            return [-1, -1]

        def binarySearch(target: float, L: int, R: int) -> int:
            while(L <= R):
                mid = (L + R) >> 1
                if (nums[mid] <= target):
                    L = mid + 1
                else:
                    R = mid - 1
            return L

        start = binarySearch(target - 0.1, 0, size - 1)
        if (start >= 0 and start < size) and (nums[start] != target):
            return [-1, -1]
        end = binarySearch(target + 0.1, start, size - 1)
        return [start, end - 1]
