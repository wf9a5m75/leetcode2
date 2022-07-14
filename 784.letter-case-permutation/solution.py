class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:

        N = len(s)
        def helper(i: int, prefix: str) -> List[str]:
            if (i == N):
                return [prefix]

            results = helper(i + 1, prefix + s[i])
            if (s[i].isalpha()):
                if (s[i].islower()):
                    results += helper(i + 1, prefix + s[i].upper())
                else:
                    results += helper(i + 1, prefix + s[i].lower())
            return results
        return helper(0, "")
                
