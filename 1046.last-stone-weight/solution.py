class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        stones.sort()

        size = len(stones)
        while(size > 2):
            top = stones.pop()
            top2 = stones.pop()

            if top == top2:
                size -= 2
            else:
                x = top - top2
                L = 0
                R = size - 3
                while(L <= R):
                    mid = (L + R) >> 1
                    if (stones[mid] < x):
                        L = mid + 1
                    else:
                        R = mid - 1
                stones.insert(L, x)
                size -= 1

        if (len(stones) == 1):
            return stones[0]
        return stones[1] - stones[0]
