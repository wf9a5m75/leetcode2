# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        results = []
        q = [root]
        isFlipping = False

        while(q):
            nextQ = []
            row = []
            while(q):
                node = q.pop(0)
                if isFlipping:
                    row.insert(0, node.val)
                else:
                    row.append(node.val)

                if node.left:
                    nextQ.append(node.left)
                if node.right:
                    nextQ.append(node.right)
            q = nextQ
            results.append(row)
            isFlipping = not isFlipping
        return results
