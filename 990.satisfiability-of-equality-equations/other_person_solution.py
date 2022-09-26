class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        p = { chr(ord('a')+c): chr(ord('a')+c) for c in range(26)}
        rank = { chr(ord('a')+c): 0 for c in range(26)}

        def find(i):
            while p[i] != i:
                i = p[i]
            return i

        def union(i, j):
            i, j = find(i), find(j)
            if i == j:
                return
            if rank[i] < rank[j]:
                p[i] = j
            elif rank[i] > rank[j]:
                p[j] = i
            else:
                p[j] = i
                rank[i] += 1

        not_eq = []

        for eq in equations:
            v1 = eq[0]
            v2 = eq[-1]
            is_equal = eq[1:3] == "=="
            if is_equal:
                union(v1, v2)
            else:
                not_eq.append([v1, v2])

        for v1, v2 in not_eq:
            if find(v1) == find(v2):
                return False

        return True
