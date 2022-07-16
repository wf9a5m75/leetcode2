class Solution:
    def validPalindrome(self, s: str) -> bool:

        def helper(s: str, canDelete: bool) -> bool:
            L = 0
            R = len(s) - 1
            while(L <= R):
                if (s[L] == s[R]):
                    L += 1
                    R -= 1
                else:
                    if (canDelete):
                        return (helper(s[L: R], False) or
                                helper(s[L + 1: R + 1], False))
                    else:
                        return False
            return True
        return helper(s, True)
