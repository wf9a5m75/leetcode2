class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 1):
            return x == 0

        orgX = x
        y = 0
        while(x > 0):
            y = y * 10 + x % 10
            x = x // 10

        return y == orgX
