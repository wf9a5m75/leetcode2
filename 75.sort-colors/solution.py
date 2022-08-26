class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroIdx, oneIdx, twoIdx = 0, 0, len(nums) - 1
        while(oneIdx <= twoIdx):
            if (nums[oneIdx] == 0):
                nums[zeroIdx], nums[oneIdx] = nums[oneIdx], nums[zeroIdx]
                zeroIdx += 1
                oneIdx += 1
            elif nums[oneIdx] == 1:
                oneIdx += 1
            else:
                nums[oneIdx], nums[twoIdx] = nums[twoIdx], nums[oneIdx]
                twoIdx -= 1
        
