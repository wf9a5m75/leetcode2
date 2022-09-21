class Solution:
    def removeStars(self, s: str) -> str:
        s = list(s)
        L = R = 0
        size = len(s)
        while(R < size):
            if (s[R] == "*"):
                L -= 1
            else:
                s[L] = s[R]
                L += 1
            R += 1

        ans = ""
        for i in range(L):
            ans += s[i]
        return ans
