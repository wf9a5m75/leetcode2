class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sDict = {}
        tDict = {}

        size = len(s)
        commonCnt = 0
        for i in range(size):
            sChar = s[i]
            tChar = t[i]

            sIdx = sDict.get(sChar, 0)
            tIdx = tDict.get(tChar, 0)
            if sIdx == 0 and tIdx == 0:
                commonCnt += 1
                sDict[sChar] = commonCnt
                tDict[tChar] = commonCnt
            elif (sIdx != tIdx):
                return False
        return True
