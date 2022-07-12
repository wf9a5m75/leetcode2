from typing import List

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        N = len(mat)

        matches = [True, True, True, True]
        for j in range(N):
            for i in range(N):
                val = mat[j][i]

                # rotated 0 deg
                matches[0] = matches[0] and (val == target[j][i])

                # rotated 90 deg
                matches[1] = matches[1] and (val == target[i][N - j - 1])

                # rotated 180 deg
                matches[2] = matches[2] and (val == target[N - j - 1][N - i - 1])

                # rotated 270 deg
                matches[3] = matches[3] and (val == target[N - i - 1][j])

                print(i,j, matches)

        return matches[0] or matches[1] or matches[2] or matches[3]

instance = Solution()

# rotate 90
print(instance.findRotation([[1, 2],[3, 4]], [[3, 1], [4, 2]]))

# rotate 180
print(instance.findRotation([[1, 2],[3, 4]], [[4, 3], [2, 1]]))

# rotate 270
print(instance.findRotation([[1, 2],[3, 4]], [[2, 4], [1, 3]]))
