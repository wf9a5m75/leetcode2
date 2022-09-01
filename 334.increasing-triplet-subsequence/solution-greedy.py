class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        size = len(nums)
        if (len(nums) < 3):
            return False

        smallest = middle = float("inf")
        for num in nums:
            if num <= smallest:
                smallest = num

            # Since the current middle is the value appearred before,
            # so, we need to change the middle to the num
            elif middle >= num:
                middle = num

            else:
                return True
        return False
