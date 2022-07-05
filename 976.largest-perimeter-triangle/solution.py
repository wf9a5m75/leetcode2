class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:

        # How to determine if three side lengths are a triangle.
        # https://www.wikihow.com/Determine-if-Three-Side-Lengths-Are-a-Triangle
        #
        # A + B > C
        # B + C > A
        # C + A > B
        #

        nums.sort()
        largest = 0
        for i in range(len(nums) - 3, -1, -1):

            if ((nums[i] + nums[i + 1] > nums[i + 2]) and
                (nums[i + 1] + nums[i + 2] > nums[i]) and
                (nums[i + 2] + nums[i] > nums[i + 1])):
                perimeter = nums[i] + nums[i + 1] + nums[i + 2]
                if (perimeter > largest):
                    largest = perimeter
                else:
                    break
        return largest
