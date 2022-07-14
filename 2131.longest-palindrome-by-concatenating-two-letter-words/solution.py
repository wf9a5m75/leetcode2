class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        mem = defaultdict(int)
        unpaired = ans = 0
        for word in words:
            if (word[0] == word[1]):
                if (mem[word] > 0):
                    #
                    # If the same word has been appearred before,
                    # we can make a pair.
                    #
                    unpaired -= 1
                    mem[word] -= 1
                    ans += 4
                else:
                    #
                    # Mark the word as appearred tentatively.
                    #
                    unpaired += 1
                    mem[word] += 1
            else:
                mirror = word[::-1]
                if (mem[mirror] > 0):
                    #
                    # If mirror word has been appearred before,
                    # we can make a pair
                    #
                    ans += 4
                    mem[mirror] -= 1
                else:
                    #
                    # Mark the word as appearred tentatively.
                    #
                    mem[word] += 1

        # If the word already palindrome is remained,
        # we can use it as the center.
        # e.g. "ccaabbccbbaacc"
        if unpaired > 0:
            ans += 2
        return ans
