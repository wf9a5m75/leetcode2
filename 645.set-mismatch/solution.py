class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s = (n * (n + 1)) >> 1
        total = 0

        duplicate = 0
        for val in nums:
            absVal = abs(val)
            total += absVal

            if nums[absVal - 1] < 0:
                duplicate = absVal
            else:
                nums[absVal - 1] *= -1

        lostNum  = s - total + duplicate
        return [duplicate, lostNum]
