class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        idx = len(num) - 1
        carryUp = 0
        while (idx >= 0) or (k > 0) or (carryUp > 0):
            if (idx >= 0):
                s = num[idx] + carryUp + (k % 10)
                num[idx] = s % 10
                idx -= 1
            else:
                s = carryUp + (k % 10)
                num.insert(0, s % 10)
            k = k // 10
            carryUp = s // 10

        return num
