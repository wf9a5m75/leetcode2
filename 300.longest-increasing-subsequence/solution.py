from typing import List
from functools import cmp_to_key

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        def compare(a: List[int], b: List[int]) -> int:
            if (a[1] != b[1]):
                return a[1] - b[1]
            return a[0] - b[0]

        size = len(nums)
        nums2 = []
        for i in range(size):
            nums2.append([i, nums[i]])

        nums2.sort(key = cmp_to_key(compare))

        print(nums2)

        cnt = 1
        i = 0
        prev = nums2[0]
        while(i < size):

            L = i + 1
            R = size - 1
            target = nums2[i][1] + 0.5

            while(L <= R):
                mid = (L + R) >> 1
                if nums2[mid][1] < target:
                    L = mid + 1
                else:
                    if (nums2[mid][0] < nums2[i][0]):
                        L = mid + 1
                    else:
                        R = mid - 1
            if (L < size):
                cnt += 1
            i = L

            print(i)

        return cnt

print(Solution().lengthOfLIS([10,9,2,5,3,7,101,18]))
