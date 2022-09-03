class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:

        results = []
        @cache
        def dfs(curr: int, n: int) -> None:
            if n == 0:
                results.append(curr)
                return
            digit = curr % 10
            if (digit + k < 10):
                dfs(curr * 10 + (digit + k), n - 1)
            if (digit - k >= 0):
                dfs(curr * 10 + (digit - k), n - 1)

        for i in range(1,10):
            dfs(i, n - 1)
        return results
