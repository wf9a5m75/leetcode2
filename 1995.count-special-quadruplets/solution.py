class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:

        size = len(nums)
        mem = {}
        for i, num in enumerate(nums):
            indicies = mem.get(num, [])
            indicies.append(i)
            mem[num] = indicies

        result = 0
        for i in range(size - 2):
            for j in range(i + 1, size - 1):
                for k in range(j + 1, size):
                    s = nums[i] + nums[j] + nums[k]
                    if s in mem:
                        L = 0
                        R = len(mem[s]) - 1
                        while(L <= R):
                            mid = (L + R) >> 1
                            if (mem[s][mid] <= k):
                                L = mid + 1
                            else:
                                R = mid - 1
                        result += len(mem[s]) - L
        return result
