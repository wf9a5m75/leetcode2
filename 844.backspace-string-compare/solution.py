class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sLen = len(s)
        tLen = len(t)

        sStr = []
        tStr = []

        for char in s:
            if (char == "#"):
                if (len(sStr)):
                    sStr.pop()
            else:
                sStr.append(char)

        for char in t:
            if (char == "#"):
                if (len(tStr)):
                    tStr.pop()
            else:
                tStr.append(char)

        return sStr == tStr
