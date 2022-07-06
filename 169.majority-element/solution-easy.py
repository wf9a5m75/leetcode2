class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        threthold = len(nums) / 2

        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            if (counts[num] >= threthold):
                return numsolution
