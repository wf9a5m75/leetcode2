class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        results = [[0] * (n + 1) for n in range(numRows)]

        results[0][0] = 1
        for i in range(numRows - 1):
            prev = 0
            for j in range(i + 1):
                results[i + 1][j] = prev + results[i][j]
                prev = results[i][j]
            results[i + 1][i + 1] = 1
        return results
