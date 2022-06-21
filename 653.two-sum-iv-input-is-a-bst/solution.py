# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        # O(N) space complexity
        mem = set()

        # O(Log N) time complexity
        def readAll(curr: Optional[TreeNode]) -> bool:
            if (curr is None):
                return False

            rest = k - curr.val
            if (rest in mem):
                return True

            mem.add(curr.val)

            if (readAll(curr.left)):
                return True
            return readAll(curr.right)
        return readAll(root)
