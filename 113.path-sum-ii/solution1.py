# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        results = []
        path = []
        def helper(root: Optional[TreeNode], rest: int) -> None:
            if (root is None):
                return

            if (root.left is None) and (root.right is None):
                if (rest == root.val):
                    results.append(path.copy() + [root.val])
                return

            path.append(root.val)
            rest -= root.val
            helper(root.left, rest)
            helper(root.right, rest)
            path.pop()
            rest += root.val

        helper(root, targetSum)

        return results
