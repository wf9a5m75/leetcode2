class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if (len(s) == 0):
            return 0
        g.sort(reverse=True)
        s.sort(reverse=True)

        cnt = 0
        sizeG = len(g)
        sizeS = len(s)

        i = 0
        j = 0
        while(i < sizeG) and (j < sizeS):
            while(i < sizeG) and (g[i] > s[j]):
                i += 1
            while(i < sizeG) and (j < sizeS) and (g[i] <= s[j]):
                i += 1
                j += 1
                cnt += 1
        return cnt
