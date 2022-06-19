#
# Two pointer approach
#   time complexity: O(N log N)
#   space complexity: O(N)
#
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expects = sorted(heights)

        mismatches = 0
        size = len(heights)
        for i in range(size):
            mismatches += 1 if heights[i] != expects[i] else 0
        return mismatches
