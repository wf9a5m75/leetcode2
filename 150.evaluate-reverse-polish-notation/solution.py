class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operaters = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "/": lambda x, y: int(x / y),
            "*": lambda x, y: x * y
        }

        for token in tokens:
            if (token in operaters):
                b = stack.pop()
                a = stack.pop()
                stack.append(operaters[token](a, b))
            else:
                stack.append(int(token))
        return stack.pop()
