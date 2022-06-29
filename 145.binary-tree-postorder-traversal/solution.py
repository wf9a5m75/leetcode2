# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        stack = []
        results = []
        while root or stack:

            # recursive call
            while root:
                results.insert(0, root.val)
                stack.append(root)
                root = root.right

            # recursive return
            root = stack.pop()
            root = root.left
        return results
