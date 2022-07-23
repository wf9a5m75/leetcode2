#
#  TC: O(m * 4n) = O(m * n)
#  SC: O(n)
#
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        N = len(l)
        results = []
        for i in range(N):

            # low = high = nums[ l[i] ]
            # mem = set()
            # for j in range(l[i], r[i] + 1):
            #     low = min(low, nums[j])
            #     high = max(high, nums[j])
            #     mem.add(nums[j])

            # O( 3 * n)
            mem = set(nums[ l[i]: r[i] + 1])
            low = min(nums[ l[i]: r[i] + 1])
            high = max(nums[ l[i]: r[i] + 1])

            if ((high - low) != 0) and (high - low) % (high - low) != 0:
                results.append(False)
                continue

            # O(n)
            diff = (high - low) // (r[i] - l[i])
            curr = low
            while(curr in mem) and (curr <= high):
                mem.remove(curr)
                curr += diff
            isArithmetic = len(mem) == 0
            results.append(isArithmetic)

        return results
