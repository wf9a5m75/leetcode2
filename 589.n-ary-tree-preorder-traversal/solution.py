"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        results = []
        stack = []
        while(stack or root):
            while(root):
                results.append(root.val)
                stack.append(root)
                if root.children:
                    root = root.children.pop(0)
                else:
                    root = None

            if stack[-1].children:
                root = stack[-1].children.pop(0)
            else:
                stack.pop()
        return results
