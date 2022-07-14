class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)

        chars = list(counts.keys())
        if (len(chars) == 1):
            return len(s)

        results = 0
        foundOdd = False
        for char in chars:
            if counts[char] & 1 == 0:
                results += counts[char]
            else:
                if foundOdd == False:
                    results += counts[char]
                    foundOdd = True
                else:
                    results += counts[char] - 1
        return results
