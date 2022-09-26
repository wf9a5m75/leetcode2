class Solution:
    def minJumps(self, arr: List[int]) -> int:
        N = len(arr)
        visited = [False] * N

        mem = {}
        for i, num in enumerate(arr):
            indicies = mem.get(num, [])
            indicies.append(i)
            mem[num] = indicies


        q = [0]
        cnt = 0
        while(q):
            nextQ = set()
            while(q):
                i = q.pop()
                if (i == N - 1):
                    return cnt
                if (visited[i]):
                    continue

                visited[i] = True

                if (i - 1 >= 0) and (not visited[i - 1]):
                    nextQ.add(i - 1)
                if (i + 1 < N) and (not visited[i + 1]):
                    nextQ.add(i + 1)

                num = arr[i]
                for j in mem[num]:
                    if (not visited[j]):
                        nextQ.add(j)
                mem[num] = []
            q = nextQ
            cnt += 1
        return -1
