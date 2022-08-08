class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        read = 0
        writeTo = 0
        k = k % size

        for _ in range(size):
            writeTo = (writeTo + k) % size

            if (writeTo == read):
                read += 1
                writeTo += 1
            else:
                nums[writeTo], nums[read] = nums[read], nums[writeTo]

                
