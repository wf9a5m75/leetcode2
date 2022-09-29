# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def convertToStr(t: TreeNode) -> str:
            if t:
                return f"#{t.val}:{convertToStr(t.left)},{convertToStr(t.right)}$"
            else:
                return "$"

        return convertToStr(subRoot) in convertToStr(root)
