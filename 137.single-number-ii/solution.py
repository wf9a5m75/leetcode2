class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        mask = 1
        single = 0
        for i in range(32):
            s = 0
            for num in nums:
                if (num & mask) > 0:
                    s += 1
                    s = s % 3

            single |= (s << i)
            mask <<= 1
        if (single >= (1 << 31)):
            single = single - (1 << 32)
        return single
