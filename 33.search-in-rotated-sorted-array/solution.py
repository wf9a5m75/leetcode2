class Solution:
    def binarySearch(self, nums: List[int], L: int, R: int, comp: Callable[[int], int]) -> List[int]:

        while(L <= R):
            mid = (L + R) >> 1
            result = comp(mid)
            if (result < 0):
                L = mid + 1
            elif (result == 0):
                return [mid, mid]
            else:
                R = mid - 1
        return [L, R]

    def debug(self, nums: List[int], L: int, R: int) -> None:

        buffer = []
        for i, num in enumerate(nums):
            if i == R:
                buffer.append(f"<R:{num}>")
            elif i == L:
                buffer.append(f"<L:{num}>")
            else:
                buffer.append(str(num))
        print(" ".join(buffer))


    def search(self, nums: List[int], target: int) -> int:

        size = len(nums)
        if (size == 1):
            return -1 if (nums[0] != target) else 0

        # 1. find the peak
        L = 0
        R = size - 1
        if (nums[0] > nums[-1]):
            L, R = self.binarySearch(nums, 0, size - 1,
                                     comp = lambda mid : -1 if (nums[mid] > nums[-1]) else 1)

        #self.debug(nums, L, R)

        # 2. find the target value
        if (nums[0] <= target) and (nums[0] <= nums[R]):
            L, R = self.binarySearch(nums, 0, R, lambda mid: nums[mid] - target)
        else:
            L, R = self.binarySearch(nums, L, size - 1, lambda mid: nums[mid] - target)

        #self.debug(nums, L, R)
        if (L < size) and (nums[L] == target):
            return L
        else:
            return -1
