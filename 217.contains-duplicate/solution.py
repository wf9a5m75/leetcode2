class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mem = set()
        for num in nums:
            if num in mem:
                return True
            mem.add(num)
        return False
