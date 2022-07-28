class TrieNode:
    def __init__(self):
        self.word = []
        self.children = {}

    def __repr__(self):
        return f"<word:[${self.word}], children: [${self.children}]>"

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        trie = TrieNode()

        # Build a trie tree
        for word in strs:

            parent = trie
            for char in sorted(word):
                if char not in parent.children:
                    parent.children[char] = TrieNode()

                parent = parent.children[char]

            parent.word.append(word)

        # Build the results
        results = []
        q = [trie]
        while(q):
            node = q.pop(0)
            if len(node.word) > 0:
                results.append(node.word)

            for char in node.children.keys():
                q.append(node.children[char])
        return results
