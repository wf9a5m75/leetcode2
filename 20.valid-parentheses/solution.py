class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        stack = []
        for char in s:
            if (char == "{") or (char == "[") or (char == "("):
                stack.append(char)
            else:
                if (len(stack) == 0) or (pairs[char] != stack[-1]):
                    return False

                lastPair = stack.pop()

        return len(stack) == 0
