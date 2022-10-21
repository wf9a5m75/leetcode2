class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mem = {}
        M_INF = -float("inf")

        for i, val in enumerate(nums):
            prevIdx = mem.get(val, M_INF)
            if i - prevIdx <= k:
                return True
            mem[val] = i
        return False
