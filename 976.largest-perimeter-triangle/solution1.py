class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # How to determine if three side lengths are a triangle.
        # https://www.wikihow.com/Determine-if-Three-Side-Lengths-Are-a-Triangle
        #
        # A + B > C
        # B + C > A
        # C + A > B
        #
        nums.sort(reverse = True)

        size = len(nums)
        result = 0
        for i in range(2, size):
            A, B, C = nums[i - 2], nums[i - 1], nums[i]

            if (A + B > C) and (A + C > B) and (B + C > A):
                return A + B + C

        return result
