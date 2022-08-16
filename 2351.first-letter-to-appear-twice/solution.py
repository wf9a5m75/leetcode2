class Solution:
    def repeatedCharacter(self, s: str) -> str:
        appear = 0

        ordA = ord("a")
        for char in s:
            mask = 1 << (ord(char) - ordA)
            if ((appear & mask) != 0):
                return char
            appear |= mask
