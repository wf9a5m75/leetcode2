class Task:
    def __init__(self):
        self.word = ""
        self.n = 0

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        current = Task()
        for char in s:
            if char.isnumeric():
                current.n = current.n * 10 + int(char)
            elif char == "[":
                stack.append(current)
                current = Task()
            elif char == "]":
                word = current.word
                current = stack.pop()
                current.word += word * current.n
                current.n = 0
            else:
                current.word += char

        return current.word
