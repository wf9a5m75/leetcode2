class Solution:
    def romanToInt(self, s: str) -> int:
        patterns = [
            ["I", 1], ["IV", 4], ["IX", 9],
            ["V", 5],
            ["X", 10], ["XL", 40], ["XC", 90],
            ["L", 50],
            ["C", 100], ["CD", 400], ["CM", 900],
            ["D", 500],
            ["M", 1000]
        ]

        # Create a trie tree
        root = {}
        for pattern in patterns:
            parent = root
            for char in pattern[0]:
                if char in parent:
                    parent = parent[char]
            parent[char] = {
                "value": pattern[1]
            }


        # Calculate the input 's'
        result = 0
        i = 0
        size = len(s)
        parent = root
        while(i < size):

            char = s[i]

            if char in parent:
                parent = parent[char]
                i += 1
            else:
                result += parent["value"]
                parent = root

        result += parent["value"]
        return result
