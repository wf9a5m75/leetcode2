#
# TC: O(2N) -> O(N)
# SC: O(N)
#
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        N = len(nums)
        results = [-1] * N
        mstack = []

        for j in range(2):
            i = N - 1
            while(i >= 0):
                while(mstack) and (nums[i] >= mstack[-1]):
                    mstack.pop()
                if (len(mstack) > 0):
                    results[i] = mstack[-1]

                mstack.append(nums[i])
                i -= 1
        return results
