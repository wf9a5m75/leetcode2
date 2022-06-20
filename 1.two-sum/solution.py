#
#   time complexity: O(N)
#   space complexity: O(N)
#
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem = {}
        for i in range(len(nums)):
            num = nums[i]
            rest = target - num
            if (rest in mem):
                return [ i, mem[rest] ]
            else:
                mem[num] = i
        return []
