class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indices = {}
        size = len(nums)
        for i in range(size):
            num = nums[i]
            if (num in indices) and (i - indices[num] <= k):
                return True
            indices[num] = i

        return False
