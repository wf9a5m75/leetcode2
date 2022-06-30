# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def findPath(curr: TreeNode, target: TreeNode, path: List[TreeNode]) -> bool:
            if (curr == target):
                path.append(target)
                return True
            if (curr is None):
                return False

            path.append(curr)

            result = findPath(curr.left, target, path)
            if (result):
                return result

            result = findPath(curr.right, target, path)
            if (not result):
                path.pop()

            return result

        pPath = []
        qPath = []
        findPath(root, p, pPath)
        findPath(root, q, qPath)

        lastNode = root
        while (pPath and qPath) and (pPath[0] == qPath[0]):
            lastNode = pPath.pop(0)
            qPath.pop(0)

        return lastNode
