class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def helper(curr: int, k: int) -> List[List[int]]:
            if (k == 0):
                return [[]]

            results = []
            for i in range(curr, n + 1):
                another = helper(i + 1, k - 1)
                for result in another:
                    result.insert(0, i)
                    results.append(result)
            return results
        return helper(1, k)
