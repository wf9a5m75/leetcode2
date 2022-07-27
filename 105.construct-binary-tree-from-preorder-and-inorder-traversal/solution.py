# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        size = len(preorder)

        global preIdx
        preIdx = 0
        def helper(L: int, R: int) -> Optional[TreeNode]:
            global preIdx
            if (L > R):
                return None

            root = TreeNode(preorder[preIdx])

            # find the center of the inorder list
            C = inorder.index(preorder[preIdx])

            preIdx += 1
            root.left = helper(L, C - 1)
            root.right = helper(C + 1, R)

            return root

        return helper(0, size - 1)
        
