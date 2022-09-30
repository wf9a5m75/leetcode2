class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        # Records the first index of each character appeared first time
        firstPositions = [-1] * 26
        for i, c in enumerate(s):
            idx = ord(c) - 97
            if firstPositions[idx] == -1:
                # This character appears first time
                firstPositions[idx] = i

        # Finding the first index of the partion from the last to the start.
        # The first index is updated by the first position of each character.
        results = []
        L = R = len(s) - 1
        for i in range(len(s) - 1, -1, -1):

            idx = ord(s[i]) - 97
            L = min(L, firstPositions[idx])

            # If the first position of the partion equals with i,
            # this is the beginning of the partion.
            if (L == i):
                results.insert(0, R - L + 1)
                R = i - 1

        return results
