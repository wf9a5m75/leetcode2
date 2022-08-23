#
# Greedy approach
#   time complexity: O(N)
#   space complexity: O(1)
#
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        i = j = float("inf")
        for num in nums:
            if (num <= i):
                i = num  # smallest
            elif (num <= j):
                j = num  # middle
            else:
                return True  # (i < num) and (j < num)

        return False
