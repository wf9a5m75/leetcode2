# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if (root is None):
            return []

        results = []
        q = [root]
        while(q):
            nextQ = []
            lastVal = -200
            while(q):
                curr = q.pop(0)
                lastVal = curr.val

                if (curr.left):
                    nextQ.append(curr.left)
                if (curr.right):
                    nextQ.append(curr.right)
            results.append(lastVal)

            q = nextQ
        return results
