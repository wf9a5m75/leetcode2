#
# Greedy:
#   Time complexity: O(N)
#   Space complexity: O(N)
#
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        first = [-1] * 26
        last = [-1] * 26

        ordA = 97
        for i, char in enumerate(s):
            cIdx = ord(char) - ordA
            if (first[cIdx] == -1):
                first[cIdx] = i
            last[cIdx] = i

        results = []
        currStart = currLast = 0
        for i, char in enumerate(s):

            if currLast + 1 == i:
                results.append(currLast - currStart + 1)
                currStart = i

            cIdx = ord(char) - ordA
            currStart = min(currStart, first[cIdx])
            currLast = max(currLast, last[cIdx])

        results.append(currLast - currStart + 1)
        return results
