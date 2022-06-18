#
# Two pointer approach
#   time complexity: O(N)
#   space complexity: O(1)
#
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pread = pwrite = 1
        size = len(nums)
        lastVal = nums[0]
        while(pread < size):
            if (nums[pread] != lastVal):
                lastVal = nums[pread]
                nums[pwrite] = nums[pread]
                pwrite += 1

            pread += 1

        return pwrite
