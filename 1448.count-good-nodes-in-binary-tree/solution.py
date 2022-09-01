# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        global count

        count = 0
        def dfs(currMax: int, currNode: TreeNode) -> None:
            global count

            if currNode is None:
                return

            if currNode.val >= currMax:
                count += 1
                currMax = currNode.val

            dfs(currMax, currNode.left)
            dfs(currMax, currNode.right)

        dfs(-10 ** 5, root)
        return count

            
