class Solution:
    def maxDepth(self, s: str) -> int:
        pCnt = 0
        result = 0
        for char in s:
            if (char == "("):
                pCnt += 1
                result = max(result, pCnt)
            elif (char == ")"):
                pCnt -= 1
        return result
