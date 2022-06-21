class Solution:
    def __init__(self):
        self.mem = {
            0: 0,
            1: 1
        };

    def fib(self, n: int) -> int:
        if (n in self.mem):
            return self.mem[n]

        result = self.fib(n - 2) + self.fib(n - 1)
        self.mem[n] = result
        return result
        
