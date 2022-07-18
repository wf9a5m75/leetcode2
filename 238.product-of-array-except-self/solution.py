class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroCnt = 0
        product = 1
        for num in nums:
            if num == 0:
                zeroCnt += 1
            else:
                product *= num

        if zeroCnt > 1:
            for i in range(len(nums)):
                nums[i] = 0
            return nums
        for i in range(len(nums)):
            if (nums[i] != 0):
                if (zeroCnt == 0):
                    nums[i] = int(product / nums[i])
                else:
                    nums[i] = 0
            else:
                nums[i] = product
        return nums
