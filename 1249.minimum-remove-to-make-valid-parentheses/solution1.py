class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        cntL = 0
        for char in s:
            if char == "(":
                cntL += 1
            elif (char == ")"):
                if (cntL == 0):
                    continue
                cntL -= 1
            stack.append(char)

        result = ""
        cntR = 0
        while(stack):
            char = stack.pop()
            if (char == ")"):
                cntR += 1
            elif (char == "("):
                if (cntR == 0):
                    continue
                cntR -= 1
            result = char + result
        return result
