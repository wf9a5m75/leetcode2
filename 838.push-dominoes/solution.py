class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        N = len(dominoes)
        force = [0] * N

        # Populate forces going from left to right
        f = 0
        for i in range(N):
            if dominoes[i] == "R":
                f = N
            elif dominoes[i] == "L":
                f = 0
            else:
                f = max(f - 1, 0)

            force[i] += f
        # Populate forces going from right to left
        f = 0
        for i in range(N - 1, -1, -1):
            if dominoes[i] == "L":
                f = N
            elif dominoes[i] == "R":
                f = 0
            else:
                f = max(f - 1, 0)
            force[i] -= f

        results = []
        for f in force:
            if f == 0:
                results.append(".")
            elif f > 0:
                results.append("R")
            else:
                results.append("L")
        return "".join(results)
        
