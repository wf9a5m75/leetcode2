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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        orgRoot = root
        q = [root]
        while(q):
            nextQ = []
            while(q):
                root = q.pop(0)
                if (root):
                    if (q):
                        root.next = q[0]
                    nextQ.append(root.left)
                    nextQ.append(root.right)
            q = nextQ
        return orgRoot
