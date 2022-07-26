class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        buffer = list(s)
        for i, char in enumerate(buffer):

            if (char == "("):
                stack.append(i)
            elif (char == ")"):
                if (len(stack)):
                    stack.pop()
                else:
                    buffer[i] = ""

        for position in stack:
            buffer[position] = ""

        return "".join(buffer)
