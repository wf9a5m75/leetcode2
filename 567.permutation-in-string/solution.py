# Time complexity: O(len(s1) + len(s2))
# Space complexity: O(2 * len(s1))

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # TC: O(len(s1))
        # SC: O(len(s1))
        orgCharCnts = Counter(s1)

        lenS1 = len(s1)
        lenS2 = len(s2)
        L = R = 0
        charCnts = orgCharCnts.copy()

        # TC: O(len(s2))
        while(R < lenS2):

            # print(f"L = {L} ({s2[L]}), R = {R} ({s2[R]})")

            if (s2[R] in charCnts):
                if (charCnts[ s2[R] ] > 0):
                    charCnts[ s2[R] ] -= 1
                    R += 1

                    if (R - L == lenS1):
                        return True
                else:
                    charCnts[ s2[L] ] += 1
                    L += 1

            else:
                # print("--->reset")
                L = R = R + 1
                charCnts = orgCharCnts.copy()

        return False
