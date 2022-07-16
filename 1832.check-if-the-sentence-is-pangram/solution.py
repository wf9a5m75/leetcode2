class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        size = len(sentence)
        if size < 26:
            return False
        aOrd = ord('a')
        appearred = 0

        for char in sentence:
            bit = ord(char) - aOrd
            appearred |= 1 << bit

        return appearred == 0x3FFFFFF1832
