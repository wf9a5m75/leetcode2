#
# Two pointer approach
#  time complexity : O(N)
#  space complexity: O(1)
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        pwrite = 0
        pread = 0
        size = len(arr)
        while(pwrite < size):
            val = arr[pread] & 0xF
            if (val == 0):
                pwrite += 1
            else:
                arr[pwrite] = (val << 4) | arr[pwrite]
            pwrite += 1
            pread += 1

        for i in range(size):
            arr[i] = arr[i] >> 4
