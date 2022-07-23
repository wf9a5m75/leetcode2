#
# TC: O(nums1.length + nums2.length)
# SC: O(nums2.length)
#
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mstack = []
        mem = {}

        i = len(nums2) - 1
        while(i >= 0):
            while(mstack) and (nums2[i] > nums2[ mstack[-1] ]):
                mstack.pop()
            if (len(mstack) == 0):
                mem[ nums2[i] ] = -1
            else:
                mem[ nums2[i] ] = nums2[ mstack[-1] ]

            mstack.append(i)
            i -= 1

        results = []
        for num1 in nums1:
            results.append(mem[num1])
        return results
