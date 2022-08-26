class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        mem = set()
        j = 1
        for i in range(31):
            mem.add("".join(sorted(list(str(j)))))
            j <<= 1

        nStr = "".join(sorted(list(str(n))))
        return nStr in mem
