# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        BOTTOM_LIMIT = -2**31
        UPPER_LIMIT = 2**31 - 1

        def validation(root: TreeNode, lowerLimit: int, upperLimit: int)-> bool:
            if (root is None):
                return True
            if (root.val < lowerLimit) or (root.val > upperLimit):
                return False

            return (validation(root.left, lowerLimit, root.val - 1) and
                    validation(root.right, root.val + 1, upperLimit))

        return (validation(root.left, BOTTOM_LIMIT, root.val - 1) and
                validation(root.right, root.val + 1, UPPER_LIMIT))
