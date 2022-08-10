class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)

        result = 0
        hasOne = 0
        for char in counts.keys():
            # We can optimize this calculation:
            #   (counts[char] // 2) * 2
            #
            # with bit masking.
            #
            # Maximum s.length = 2000,
            # so it's 11 bits.
            # Thus 0x7FE is enough.
            result += counts[char] & 0x7FE

            # Only one character can be placed as center.
            hasOne = hasOne | (counts[char] & 1)

        return result + hasOne
