# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:

        def helper(curr: Optional[TreeNode]) -> str:
            if (curr is None):
                return ""

            result = f"{curr.val}"
            if (curr.left or curr.right):
                result = f"{result}({helper(curr.left)})"

            if (curr.right):
                result = f"{result}({helper(curr.right)})"

            return result
        return helper(root)
