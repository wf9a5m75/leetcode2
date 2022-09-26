class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if arr[start] == 0:
            return True

        size = len(arr)
        q = [start]
        while(q):
            i = q.pop(0)
            if arr[i] < 0:
                # already visited
                continue
            if arr[i] == 0:
                return True

            if (i + arr[i] < size):
                q.append(i + arr[i])

            if (i - arr[i] >= 0):
                q.append(i - arr[i])

            arr[i] = -arr[i]
        return False
