class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        L = 0
        R = len(s) - 1
        while(L < R):
            if (not s[L].isnumeric()) and (not s[L].isalpha()):
                L += 1
                continue
            if (not s[R].isnumeric()) and (not s[R].isalpha()):
                R -= 1
                continue

            if (s[L] == s[R]):
                L += 1
                R -= 1
            else:
                return False
        return True
