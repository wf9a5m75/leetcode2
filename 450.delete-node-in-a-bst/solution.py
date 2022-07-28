# https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minValueNode(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        while(node.left):
            node = node.left
        return node

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if (root is None):
            return None

        if (key < root.val):
            root.left = self.deleteNode(root.left, key)
        elif (key > root.val):
            root.right = self.deleteNode(root.right, key)
        else:

            # Node with only one child or no child
            if (root.left is None):
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp


            # Node with two children:
            # Get the inorder successor
            # (smallest in the right subtree)
            temp = self.minValueNode(root.right)

            # Copy the inorder successor's content to this node
            root.val = temp.val

            # Delete the inorder successor
            root.right = self.deleteNode(root.right, temp.val)

        return root
