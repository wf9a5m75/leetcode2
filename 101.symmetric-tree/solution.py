# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def checker(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            if (left is None) and (right is None):
                return True

            if (((left is None) and  right) or
                (left and right is None) or
                (left.val != right.val)):
                return False
            return checker(left.left, right.right) and checker(left.right, right.left)
        return checker(root.left, root.right)
