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


"""
[23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
19
[28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58, 61, 64, 67, 70, 1, 4, 7, 10, 13, 16, 19, 22, 25]
25
[9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77, 81, 85, 1, 5]
9
[25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58, 61, 64, 67, 1, 4, 7, 10, 13, 16, 19, 22]
67
[16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58, 1, 4, 7, 10, 13]
1
[1, 3]
3
[5, 9, 13, 17, 1]
17
[4, 1]
1
[4, 1]
4
[1, 4, 7, 10, 13, 16, 19, 22, 25]
1
[1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77, 81, 85, 89]
41
[1,3]
4
[3,1]
4
[3,1]
0
[1,3]
2
[1]
0
[0]
2
[1,3,5]
3
[4,5,6,7,0,1,2]
0
[4,5,6,7,0,1,2]
3
[1]
0
"""
