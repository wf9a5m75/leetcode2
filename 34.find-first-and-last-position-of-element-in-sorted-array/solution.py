class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        if (size == 0) or (target < nums[0]) or (target > nums[-1]):
            return [-1, -1]

        start = self.binarySearch(nums, target - 0.5)
        if (start + 1 == size) or (nums[start + 1] != target):
            return [-1, -1]

        end = self.binarySearch(nums, target + 0.5)
        return [start + 1, end]


    def binarySearch(self, nums: List[int], target: float) -> int:
        # print(f'target = {target}')
        L = 0
        R = len(nums) - 1
        while(L <= R):
            mid = (L + R) >> 1
            if (nums[mid] <= target):
                L = mid + 1
            else:
                R = mid - 1
        return R
