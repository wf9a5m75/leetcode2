class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mem = {
            0: 1
        }

        total = 0
        result = 0

        for num in nums:
            total += num
            result += mem.get(total - k, 0)
            mem[total] = mem.get(total, 0) + 1

        return result
