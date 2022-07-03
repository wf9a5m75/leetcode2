class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 1) or (x % 10 == 0):
            return x == 0

        orgX = x
        y = 0
        while(x > y):
            y = y * 10 + x % 10
            x = x // 10

        return y == x or y // 10 == x
