class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        flowerbed.insert(0, 0)
        flowerbed.append(0)

        size = len(flowerbed)
        cnt = 0
        i = 0
        while(i < size) and (n > 0):
            if (flowerbed[i] == 0):
                cnt += 1
                if cnt == 3:
                    n -= 1
                    cnt = 1
            else:
                cnt = 0
            i += 1
        return n == 0
