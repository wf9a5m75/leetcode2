class Solution:
    def __init__(self):
        self.mem = {
            0: [""],
            1: ["()"]
        }

    def generateParenthesis(self, n: int) -> List[str]:
        if (n in self.mem):
            return self.mem[n]

        results = []
        for i in range(n):
            for left in self.generateParenthesis(i):
                for right in self.generateParenthesis(n - i - 1):
                    results.append(f"({left}){right}")
        self.mem[n] = results

        return results
