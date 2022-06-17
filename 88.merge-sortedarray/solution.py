# two pointers approach
#
#   time complexity: O(N log N)
#   space complexity: O(1)
#
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1
        p2 = n - 1
        pW = m + n - 1
        while(p1 >= 0) and (p2 >= 0):
            if (nums1[p1] >= nums2[p2]):
                nums1[pW] = nums1[p1]
                p1 -= 1
            else:
                nums1[pW] = nums2[p2]
                p2 -= 1
            pW -= 1

        while(p2 >= 0):
            nums1[pW] = nums2[p2]
            pW -= 1
            p2 -= 1
