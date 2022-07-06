class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carryUp = 1
        j = len(digits) - 1
        while(j >= 0):
            s = digits[j] + carryUp
            carryUp = 1 if (s > 9) else 0
            digits[j] = s % 10
            j -= 1
        if carryUp == 1:
            digits.insert(0, 1)
        return digits
