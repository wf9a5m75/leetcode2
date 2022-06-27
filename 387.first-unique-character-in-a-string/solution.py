class Solution:
    def firstUniqChar(self, s: str) -> int:
        counters = defaultdict(lambda x: 0)
        for i, c in enumerate(s):
            if c not in counters:
                counters[c] = i
            else:
                counters[c] = -1

        firstIdx = len(s) + 1
        for c in counters.keys():
            if (counters[c] != -1):
                firstIdx = min(firstIdx, counters[c])

        if (firstIdx == len(s) + 1):
            return -1
        else:
            return firstIdx
