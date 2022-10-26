class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mem = {0 : 0}  # sum -> index
        s = 0
        for i, val in enumerate(nums):
            s += val
            r = s % k
            if r not in  mem:
                # Since the question requires the subarray at least two elements,
                # so, we keep the valid index (i + 1)
                #
                # This prevents the case, such as:
                #     nums = [3, 0], k = 3
                mem[r] = i + 1
            elif mem[r] < i:
                return True
        return False
