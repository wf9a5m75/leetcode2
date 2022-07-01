class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        L = 0
        R = 0
        N = len(s)
        while(R < N):
            while(R < N) and (s[R] != " "):
                R += 1
            nextPos = R + 1
            R -= 1
            while(L < R):
                s[L], s[R] = s[R], s[L]
                L += 1
                R -= 1
            L = R = nextPos
        return "".join(s)
