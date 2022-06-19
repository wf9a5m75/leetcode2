#
# Counter sort approach
#  time complexity: O(N)
#  space complexity: O(kind of heights)
#
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        counter = [0] * 101
        for height in heights:
            counter[height] += 1

        result = 0
        curHeight = 0
        for i in range(len(heights)):
            # Find the next expected value
            while(counter[curHeight] == 0):
                curHeight += 1

            if (curHeight != heights[i]):
                result += 1
            counter[curHeight] -= 1

        return result
