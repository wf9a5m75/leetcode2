class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        N = len(graph)

        results = []
        def dfs(i: int, path: List[int]) -> None:
            path.append(i)
            if (i == N - 1):
                results.append(path.copy())
                path.pop()
                return

            for c in graph[i]:
                dfs(c, path)
            path.pop()
        dfs(0, [])
        return results
