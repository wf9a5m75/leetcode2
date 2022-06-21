# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if (root is None):
            return 0
        def helper(curr: TreeNode, depth: int) -> int:

            # leaf
            if (curr.left is None) and (curr.right is None):
                return depth

            result = 100000
            if (curr.left is not None):
                result = helper(curr.left, depth + 1)

            if (curr.right is not None):
                result = min(result, helper(curr.right, depth + 1))

            return result
        return helper(root, 1)
