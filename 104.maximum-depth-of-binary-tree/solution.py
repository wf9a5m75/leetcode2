#
# Time complexity: O(N)  N denotes the number of nodess
# Space complexity: O(1)
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def helper(curr: Optional[TreeNode]) -> int:
            if (curr is None):
                return 0
            return max(helper(curr.left), helper(curr.right)) + 1
        return helper(root)
