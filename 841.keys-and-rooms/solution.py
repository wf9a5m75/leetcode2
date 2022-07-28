class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        numOfRooms = len(rooms)
        visited = [False] * numOfRooms

        def dfs(curr: int) -> bool:
            visited[curr] = True

            keys = rooms[curr]
            for key in keys:
                if (visited[key] == False):
                    dfs(key)
            return False
        dfs(0)

        for i in range(numOfRooms):
            if (visited[i] == False):
                return False
        return True
