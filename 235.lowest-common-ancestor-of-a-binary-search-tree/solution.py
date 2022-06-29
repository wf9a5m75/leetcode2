# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if (root == p) or (root == q):
            return root

        pNext = root.left if (p.val < root.val) else root.right
        qNext = root.left if (q.val < root.val) else root.right

        if (pNext != qNext):
            return root
        return self.lowestCommonAncestor(pNext, p, q)
