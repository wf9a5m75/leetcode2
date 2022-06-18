#
# Two pointer approach
#   time complexity: O(N)
#   space complexity: O(1)
#
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # Since the first element is always valid, we can start from index 1.
        pread = pwrite = 1
        lastVal = nums[0]
        cnt = 1

        # The array is sorted, therefore the same values are appeared consectively.
        # So, we can pick up the values at most two using the cnt variable.
        size = len(nums)
        while(pread < size):
            if ((nums[pread] != lastVal) or (cnt < 2)):
                cnt = 1 if (nums[pread] != lastVal) else 2
                lastVal = nums[pread]
                nums[pwrite] = nums[pread]
                pwrite += 1
            pread += 1
        return pwrite
