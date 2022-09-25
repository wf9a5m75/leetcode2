class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        table = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        size = len(digits)
        def backtrack(i: int) -> List[str]:
            if (i == size):
                return []
            d = digits[i]
            others = backtrack(i + 1)
            if (len(others) == 0):
                return table[d]

            results = []
            for char in table[d]:
                for other in others:
                    results.append(char + other)
            return results
        return backtrack(0)
