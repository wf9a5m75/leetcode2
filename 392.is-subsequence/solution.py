class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        i = 0
        lenS = len(s)
        j = 0
        lenT = len(t)

        while(i < lenS) and (j < lenT):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == lenS
