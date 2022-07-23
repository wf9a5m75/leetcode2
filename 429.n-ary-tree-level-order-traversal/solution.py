"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if (root is None):
            return []

        q = [root]
        results = []
        while(q):
            nextQ = []
            row = []
            while(q):
                root = q.pop(0)
                row.append(root.val)
                nextQ += root.children
            results.append(row)
            q = nextQ
        return results
