class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:

        parents = {
            0: 0
        }
        groups = [0] * 26
        prohibits = {}

        def findParent(x: int) -> int:
            p = parents[x]
            if (p == x):
                return p
            parents[x] = findParent(p)
            return parents[x]

        groupIdx = 0
        for eq in equations:
            charA, charB = ord(eq[0]) - 97, ord(eq[3]) - 97
            groupA, groupB = findParent(groups[charA]), findParent(groups[charB])

            if eq[1:3] == "==":
                if groupA + groupB == 0:
                    # both first time
                    groupIdx += 1
                    groups[charA] = groupIdx
                    groups[charB] = groupIdx
                    parents[groupIdx] = groupIdx

                elif (groupA == 0) or (groupB == 0):
                    # merge
                    i = max(groupA, groupB)
                    groups[charA] = i
                    groups[charB] = i

                elif (groupA != groupB):

                    # check both groups can be merged
                    if (((prohibits.get(groupA, 0) & (1 << groupB)) > 0) or
                        ((prohibits.get(groupB, 0) & (1 << groupA)) > 0)):
                        return False

                    # merge
                    groupIdx += 1

                    parents[groupA] = groupIdx
                    parents[groupB] = groupIdx
                    parents[groupIdx] = groupIdx

                    groups[charA] = groupIdx
                    groups[charB] = groupIdx
                    prohibits[groupIdx] = prohibits.get(groupA, 0) | prohibits.get(groupB, 0)

            else:
                # variable names should be different
                if charA == charB:
                    return False

                if groupA == 0:
                    groupIdx += 1
                    groupA = groupIdx
                    parents[groupA] = groupIdx
                    groups[charA] = groupIdx

                if groupB == 0:
                    groupIdx += 1
                    groupB = groupIdx
                    parents[groupB] = groupIdx
                    groups[charB] = groupIdx

                # both should be different
                if (groupA == groupB):
                    return False

                prohibits[groupA] = prohibits.get(groupA, 0) | (1 << groupB)
                prohibits[groupB] = prohibits.get(groupB, 0) | (1 << groupA)
        return True
