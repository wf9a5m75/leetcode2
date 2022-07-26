# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def helper(L: int, R: int) -> Optional[TreeNode]:
            if (L > R):
                return None
            mid = (L + R) >> 1

            root = TreeNode(nums[mid])
            root.left = helper(L, mid - 1)
            root.right = helper(mid + 1, R)
            return root

        return helper(0, len(nums) - 1)
