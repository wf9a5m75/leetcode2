class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        L = R = len(s) - 1
        while(R >= 0) and (s[R] == " "):
            R -= 1
        L = R - 1
        while(L >= 0) and (s[L] != " "):
            L -= 1
        return (R - L)
