# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = [root]
        results = []
        while(q):
            nextQ = []
            total = 0
            cnt = len(q)
            while(q):
                root = q.pop(0)
                total += root.val
                if root.left:
                    nextQ.append(root.left)
                if root.right:
                    nextQ.append(root.right)
            results.append(total / cnt)
            q = nextQ
        return results
