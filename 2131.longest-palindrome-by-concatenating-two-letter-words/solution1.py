class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        counts = Counter(words)

        maxLen = 0
        center = 0
        for key in counts.keys():
            rWords = key[::-1]
            if counts.get(rWords, 0) > 0:
                if (key == rWords):
                    maxLen += ((counts[key] // 2) * 2) * 2
                    counts[key] %= 2
                    if (center == 0) and (counts[key] == 1):
                        counts[key] = 0
                        center = 2
                else:
                    n = min(counts[rWords], counts[key])
                    counts[rWords] -= n
                    counts[key] -= n
                    maxLen += n * 4
        return maxLen + center
