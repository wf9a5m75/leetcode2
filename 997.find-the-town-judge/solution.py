#
# O(N) time, O(N) space
# https://leetcode.com/problems/find-the-town-judge/discuss/2475005/Explain-with-a-picture-and-some-test-cases
#
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        counts = [0] * n

        for graph in trust:
            counts[graph[1] - 1] += 1
            counts[graph[0] - 1] -= 1

        for i in range(n):
            if (counts[i] == n - 1):
                return i + 1

        return -1
