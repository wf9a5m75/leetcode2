class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        palindrome = list(palindrome)

        size = len(palindrome)
        if (size == 1):
            return ""
        half = size // 2
        isOddLen = size % 2 == 1

        ordA = ord("a")
        changed = False
        for i, char in enumerate(palindrome):
            if (ord(char) - 1 >= ordA):
                if (not isOddLen) or (i != half):

                    palindrome[i] = "a"
                    changed = True
                    break

        # The case for the tail is ".....a", but  palindrome is not "a".
        if (not changed):
            palindrome[size - 1] = chr(ord(palindrome[size - 1]) + 1)
            changed = True

        if (not changed):
            return ""
        return "".join(palindrome)

ins = Solution()
tests = {
    "aca": "acb",
    "abccba": "aaccba",
    "a": "",
    "aaaaccaaaa": "aaaaacaaaa",
    "acca": "aaca",
    "aa": "ab"
}
for testWord in tests.keys():
    answer = tests[testWord]
    result = ins.breakPalindrome(testWord)
    print(result == answer, f"input={testWord}, result={result}, answer={answer}")
