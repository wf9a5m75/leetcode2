# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if (root is None):
            return []

        results = []
        def dfs(curr: Optional[TreeNode], rest: int, path: List[int])->None:

            path.append(curr.val)
            rest -= curr.val

            if (curr.left is None) and (curr.right is None):
                if (rest == 0):
                    results.append(path.copy())
                path.pop()
                return
            if (curr.left):
                dfs(curr.left, rest, path)
            if (curr.right):
                dfs(curr.right, rest, path)

            path.pop()
            rest += curr.val

        dfs(root, targetSum, [])
        return results
