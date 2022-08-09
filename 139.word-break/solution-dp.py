class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        size = len(s)
        dp = [False] * (size + 1)

        dp[0] = True
        words = [ (word, len(word)) for word in wordDict ]

        for i in range(size):
            if dp[i] == False:
                continue

            nextWords = []
            for word, wordLen in words:
                if i + wordLen <= size:
                    nextWords.append((word, wordLen))

                    if s[i:i+ wordLen] == word:
                        dp[i + wordLen] = True

            if dp[size]:
                return True
            words = nextWords
        return False
