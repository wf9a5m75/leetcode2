# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def helper(root: Optional[TreeNode]) -> Optional[TreeNode]:
            if (root is None):
                return None

            # flatten the right side
            right = helper(root.right)

            # flatten the left side
            left = helper(root.left)

            if (left):
                # If the left side is not None,
                # we connect the right side after the left side.

                tail = left
                while(tail.right):
                    tail = tail.right
                tail.right = right
                root.right = left
            else:
                # otherwise, just connect the right side.
                root.right = right

            root.left = None

            return root
        helper(root)
