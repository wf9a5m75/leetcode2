import math

class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        # First, we need to know the theta and the psi angles
        angles = []

        # theta
        angles.append(math.atan(q / p))

        # psi
        angles.append(math.pi * 0.5 - angles[0])
        print(angles)

        baseLength = p

        angleIdx = 0
        turn = 0

        cnt = 0
        while(cnt < 100):
            if turn == 0:
                dst = [p, baseLength * math.tan(angles[angleIdx])]
                baseLength = p - dst[1]

            elif turn == 1:
                dst = [p - baseLength * math.tan(angles[angleIdx]) , p]
                baseLength = dst[0]

            elif turn == 2:
                dst = [0, p- baseLength * math.tan(angles[angleIdx])]
                baseLength = dst[1]

            elif turn == 3:
                dst = [baseLength * math.tan(angles[angleIdx]), 0]
                baseLength = p - dst[0]

            dst[0] = round(dst[0] * 1000) / 1000
            dst[1] = round(dst[1] * 1000) / 1000
            print(turn, dst)

            if (dst == [0, p]):
                return 2
            elif (dst == [p, p]):
                return 1
            elif (dst == [0, p]):
                return 0


            angleIdx = (angleIdx + 1) % 2
            turn = (turn + 1) % 4
            cnt += 1

print(Solution().mirrorReflection(6, 4))
