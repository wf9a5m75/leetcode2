class Solution:
    def __init__(self):
        #
        # Hamming weight
        # https://en.wikipedia.org/wiki/Hamming_weight
        #
        self.m1 = 0x55555555  # binary: 0101 0101 0101 0101 0101 0101 0101 0101
        self.m2 = 0x33333333  # binary: 0011 0011 0011 0011 0011 0011 0011 0011
        self.m4 = 0x0f0f0f0f  # binary: 0000 1111 0000 1111 0000 1111 0000 1111
        self.m8 = 0x00ff00ff  # binary: 0000 0000 1111 1111 0000 0000 1111 1111
        self.m16 = 0x0000ffff # binary: 0000 0000 0000 0000 1111 1111 1111 1111

    def hammingWeight(self, n: int) -> int:

        # print(bin(n), n)
        n = (n & self.m1) + ((n >> 1) & self.m1)

        # print(bin(n), n)
        n = (n & self.m2) + ((n >> 2) & self.m2)

        # print(bin(n), n)
        n = (n & self.m4) + ((n >> 4) & self.m4)

        # print(bin(n), n)
        n = (n & self.m8) + ((n >> 8) & self.m8)

        # print(bin(n), n)
        n = (n & self.m16) + ((n >> 16) & self.m16)

        # print(bin(n), n)
        return n
