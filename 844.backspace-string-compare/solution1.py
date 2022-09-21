class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sLen = len(s)
        tLen = len(t)

        sIdx = sLen - 1
        tIdx = tLen - 1
        tCnt = 0
        sCnt = 0

        while(sCnt + tCnt > 0) or (sIdx >= 0) or (tIdx >= 0):
            if (sIdx >= 0) and (s[sIdx] == "#"):
                sCnt += 1
                sIdx -= 1
                continue
            if (tIdx >= 0) and (t[tIdx] == "#"):
                tCnt += 1
                tIdx -= 1
                continue
            if (sCnt > 0):
                sCnt -= 1
                sIdx -= 1
                continue
            if (tCnt > 0):
                tCnt -= 1
                tIdx -= 1
                continue

            if (sIdx < 0 and tIdx >= 0) or (sIdx >= 0 and tIdx < 0) or (s[sIdx] != t[tIdx]):
                return False
            sIdx -= 1
            tIdx -= 1
        return (sIdx < 0) and (tIdx < 0)
