# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if (root is None):
            return []

        results += self.preorderTraversal(root.left)
        results = [root.val]
        results += self.preorderTraversal(root.right)

        return results
