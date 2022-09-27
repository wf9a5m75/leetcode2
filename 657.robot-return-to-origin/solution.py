class Solution:
    def judgeCircle(self, moves: str) -> bool:
        delta = [0, 0]  # dy,dx
        actions = {
            "U": lambda : delta[0] + 1,
            "D": lambda : delta[0] - 1,
            "L": lambda : delta[1] + 1,
            "R": lambda : delta[1] - 1,
        }
        for char in moves:
            idx = 0 if char == "U" or char == "D" else 1
            delta[idx] = actions[char]()
        return delta[0] == delta[1] == 0
