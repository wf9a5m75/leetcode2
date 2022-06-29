
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        stack = []
        results = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()

            # inorder traversal
            results.append(root.val)

            root = root.right
        return results
