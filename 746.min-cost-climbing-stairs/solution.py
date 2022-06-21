#
# DP approach
#   Time complexity: O(N)
#   Space complexity: O(N)
#
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        size = len(cost)

        # Start from the smaller cost position
        minCosts = [0] * size
        minCosts[0] = cost[0]
        minCosts[1] = cost[1]

        for i in range(2, size):
            minCosts[i] = cost[i] + min(minCosts[i - 1], minCosts[i - 2])


        return min(minCosts[size - 2], minCosts[size - 1])
