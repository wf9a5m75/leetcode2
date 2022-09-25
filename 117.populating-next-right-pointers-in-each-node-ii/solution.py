"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None

        orgRoot = root
        q = [root]
        while(q):
            nextQ = []
            prev = None
            while(q):
                root = q.pop(0)
                if (root.left):
                    if prev:
                        prev.next = root.left
                    prev = root.left
                    nextQ.append(root.left)

                if (root.right):
                    if prev:
                        prev.next = root.right
                    prev = root.right
                    nextQ.append(root.right)
            q = nextQ
        return orgRoot
