class Solution:
    def integerBreak(self, n: int) -> int:
        if (n == 2):
            return 1
        if (n == 3):
            return 2

        @cache
        def backtrack(rest: int)->int:
            result = 1
            if (rest - 2 >= 0):
                result = backtrack(rest - 2) * 2

            i = 3
            while(rest - i >= 0):
                result = max(result, backtrack(rest - i) * i)
                i += 2

            return result

        return backtrack(n)
            
