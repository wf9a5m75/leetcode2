class TrieNode:
    def __init__(self, char: str):
        self.char = char
        self.eow = False
        self.children = {}

    def addChar(self, char: str):
        if (char not in self.children):
            self.children[char] = TrieNode(char)

        return self.children[char]

    def nextChar(self, char: str):
        return self.children.get(char, None)

    def hasChar(self, char: str) -> bool:
        return char in self.children

    def __repr__(self):
        return f"{self.eow}:({self.children})"

class Solution:
    @cache
    def helper(self, s: str, idx: int, parent: TrieNode) -> bool:
        if idx == len(s):
            return parent and (parent.eow)

        result = False
        if parent.eow:
            result = self.helper(s, idx, self.root)

        if result == False and parent.hasChar(s[idx]):
            child = parent.nextChar(s[idx])
            result = self.helper(s, idx + 1, child)
        return result



    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        root = TrieNode("<>")
        for word in wordDict:
            parent = root
            for char in word:
                parent = parent.addChar(char)

            parent.eow = True

        self.root = root

        return self.helper(s, 0, root)
