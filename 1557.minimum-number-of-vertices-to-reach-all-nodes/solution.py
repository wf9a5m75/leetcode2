class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        possibility = [True] * n
        for edge in edges:
            possibility[edge[1]] = False
        results = []
        for i in range(n):
            if possibility[i]:
                results.append(i)
        return results
