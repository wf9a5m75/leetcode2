class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        mem = {}
        appearred = set()
        s = s.split(" ")

        idx = 0
        size1 = len(pattern)
        size2 = len(s)
        while(idx < size1) and (idx < size2):
            char = pattern[idx]
            if char in mem:
                word = mem[char]
                if s[idx] != word:
                    return False
            else:
                if s[idx] in appearred:
                    return False
                appearred.add(s[idx])
                mem[char] = s[idx]
            idx += 1
        return (idx == size1) and (idx == size2)
