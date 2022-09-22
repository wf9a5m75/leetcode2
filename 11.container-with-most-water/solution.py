#
# Two pointers
#  Time complexity: O(N)
#  Space complexity: O(1)
#
class Solution:
    def maxArea(self, height: List[int]) -> int:
        size = len(height)
        L = 0
        R = size - 1
        maxL = 0
        maxR = size - 1
        maxWater = 0
        needsUpdate = True
        while(L < R):
            if height[maxR] < height[R]:
                maxR = R
                needsUpdate = True
            if height[maxL] < height[L]:
                maxL = L
                needsUpdate = True

            if needsUpdate:
                maxWater = max(maxWater, (maxR - maxL) * min(height[maxL], height[maxR]))
            if (height[L] <= height[R]):
                L += 1
            else:
                R -= 1
            needsUpdate = False
        return maxWater
