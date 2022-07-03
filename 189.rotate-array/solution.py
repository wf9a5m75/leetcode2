class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        if (k == 0) or (size < 2):
            return

        k = k % size

        # 1. flip the array
        self.flip(nums, 0, size - 1)

        # 2. flip each segment
        self.flip(nums, 0, k - 1)
        self.flip(nums, k, size - 1)

    def flip(self, nums: List[int], L: int, R: int):
        while(L < R):
            nums[L], nums[R] = nums[R], nums[L]
            L += 1
            R -= 1
