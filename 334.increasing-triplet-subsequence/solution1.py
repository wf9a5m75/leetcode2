class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        size = len(nums)
        if (size < 3):
            return False

        values = [float("inf"), float("inf")] # smallest, middle

        for i, val in enumerate(nums):
            if (values[0] >= val):
                values[0] = val

            elif (values[1] >= val):
                values[1] = val

            else:
                return True
        return False
            
