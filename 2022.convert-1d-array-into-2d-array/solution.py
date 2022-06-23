class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        size = len(original)
        if (m * n != size):
            return []

        results = [
            [0] * n for _ in range(m)
        ]
        x = y = 0
        for i in range(size):
            results[y][x] = original[i]
            x = (x + 1) % n
            y += 1 if x == 0 else 0
        return results
