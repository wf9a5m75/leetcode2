# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        def traverse(currentQ: List[TreeNode]):
            result = []
            nextQ = []
            while currentQ:
                root = currentQ.pop(0)
                result.append(root.val)

                if (root.left):
                    nextQ.append(root.left)
                if (root.right):
                    nextQ.append(root.right)

            results = [result]
            if (nextQ):
                another = traverse(nextQ)
                results = another + results
            return results

        return traverse([root])
