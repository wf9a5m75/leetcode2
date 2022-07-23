#
#  m ... nums.length
#  n ... max(r) - max(l)
#
#  TC: O(m * n log n)
#  SC: O(n)  .... because we allocate it for results
#
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        N = len(l)
        results = []
        for i in range(N):
            subNums = nums[l[i]:r[i] + 1]
            subNums.sort()

            diff = subNums[1] - subNums[0]
            isArithmetic = True
            prev = subNums[0] - diff
            for s in subNums:
                if (prev + diff != s):
                    isArithmetic = False
                    break
                prev = s
            results.append(isArithmetic)
        return results
