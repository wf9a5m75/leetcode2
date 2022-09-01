class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)

        # - Count up the number of zero elements
        # - If we found a zero, we keep the position.
        # - If we found zeros more than one time, we can stop the loop.
        # - We calculate the overall product value.
        zeroCnt = 0
        lastZero = -1
        overall = 1
        for i, num in enumerate(nums):
            if num == 0:
                zeroCnt += 1
                if zeroCnt == 2:
                    break
                lastZero = i
            else:
                overall *= num

        if zeroCnt > 0:
            # If we found zero(s), the results are zeros.
            nums = [0] * size

            # Only the case the number of zero is one time,
            # the product value is available.
            if zeroCnt == 1:
                nums[lastZero] = overall
            return nums
        else:
            # If there is no zero, we need to calculate each value
            for i in range(size):
                nums[i] = overall // nums[i]
            return nums
        
