class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        results = []
        pCnt = Counter(p)
        pSize = len(p)
        sSize = len(s)
        sCnt = Counter(s[:pSize])
        if (sCnt == pCnt):
            results.append(0)

        for i in range(pSize, sSize):
            sCnt[s[i - pSize]] -= 1
            sCnt[s[i]] = sCnt.get(s[i], 0) + 1

            if (sCnt == pCnt):
                results.append(i - pSize + 1)
        return results
