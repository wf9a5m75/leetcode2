class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        size = len(s)
        if (size <= 10):
            return []

        mask = 0
        appear = set()
        DNA10 = s[:10]
        results = set()

        appear.add(DNA10)

        for i in range(1, size - 9):
            DNA10 = DNA10[1:] + s[i + 9]
            if DNA10 in appear:
                results.add(DNA10)
            appear.add(DNA10)

        return list(results)
