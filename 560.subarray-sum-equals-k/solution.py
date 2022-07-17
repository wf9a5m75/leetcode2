class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mem = {0 : 1}
        total = 0

        result = 0
        for num in nums:
            total = total + num
            if (total - k) in mem:
                result += mem[total - k]
            mem[total] = mem.get(total, 0) + 1
        return result
