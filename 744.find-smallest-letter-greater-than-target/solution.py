class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        size = len(letters)
        L = 0
        R = size - 1
        targetOrd = ord(target) + 0.5

        while(L <= R):
            mid = (L + R) >> 1
            midOrd = ord(letters[mid])

            if midOrd == targetOrd:
                if mid == size - 1:
                    return letters[0]
                else:
                    return letters[mid + 1]

            elif midOrd < targetOrd:
                L = mid + 1
            else:
                R = mid - 1

        R = (R + 1) % size
        return letters[R]

"""
# test cases
["c","f","j"]
"a"
["c","f","j"]
"c"
["c","f","j"]
"d"
["a","b"]
"z"
["e","e","e","e","e","e","n","n","n","n"]
"e"
"""
