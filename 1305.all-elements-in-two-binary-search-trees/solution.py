# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        list1 = self.inorder(root1)
        list2 = self.inorder(root2)

        size = len(list1)
        for num in list2:
            L = 0
            R = size - 1
            while(L <= R):
                mid = (L + R) >> 1
                if (list1[mid] <= num):
                    L = mid + 1
                else:
                    R = mid - 1
            list1.insert(L, num)
            size += 1
        return list1

    def inorder(self, root: TreeNode) -> List[int]:
        if (root is None):
            return []
        results = []
        if root.left:
            results = self.inorder(root.left)
        results.append(root.val)
        if root.right:
            results += self.inorder(root.right)
        return results
