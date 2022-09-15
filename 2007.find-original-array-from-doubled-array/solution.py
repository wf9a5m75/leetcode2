class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        size = len(changed)
        if ((size & 1) == 1):
            return []
        changed.sort()

        mem = {}
        original = []
        for num in changed:
            if mem.get(num, 0) > 0:
                original.append(num >> 1)
                mem[num] -= 1
            else:
                num2 = num << 1
                mem[num2] = mem.get(num2, 0) + 1
        if (len(original) == (size >> 1)):
            return original
        else:
            return []
