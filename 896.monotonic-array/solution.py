class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        goesUp = goesDown = True
        prev = nums[0]

        size = len(nums)
        i = 0
        while(i < size) and (goesUp or goesDown):

            goesUp = goesUp and (prev <= nums[i])
            goesDown = goesDown and (prev >= nums[i])
            prev = nums[i]
            i += 1
        return goesUp or goesDown
