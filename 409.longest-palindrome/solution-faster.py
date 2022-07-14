class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)

        result = 0
        for char in counts.keys():
            result += counts.get(char) & 0xFFFFFFFE
            if (result & 1 == 0) and (counts.get(char) & 1 == 1):
                result += 1
        return result
