class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for i, char in enumerate(s):
            last[char] = i

        R = anchor = 0
        results = []

        for L, char in enumerate(s):
            R = max(R, last[char])
            if (L == R):
                results.append(R - anchor + 1)
                anchor = L + 1
        return results
