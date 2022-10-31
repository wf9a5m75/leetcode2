class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        N = len(nums)
        flags = 2 ** (N + 1) - 1

        for num in nums:
            mask = 1 << num
            flags = flags ^ mask

        return int(math.log2(flags))
