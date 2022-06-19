class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroCnt = 0
        pread = pwrite = 0
        size = len(nums)
        while(pread < size):
            if (nums[pread] != 0):
                nums[pwrite] = nums[pread]
                pwrite += 1
            pread += 1

        while(pwrite < size):
            nums[pwrite] = 0
            pwrite += 1
        
