class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = [""]
        for c in s:
            if (c == stack[-1]):
                while(c == stack[-1]):
                    stack.pop()
            else:
                stack.append(c)
        return "".join(stack)
