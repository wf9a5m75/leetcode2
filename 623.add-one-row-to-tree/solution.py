# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:

        if (depth == 1):
            newNode = TreeNode(val)
            newNode.left = root
            return newNode


        q = [root]
        while(q):
            depth -= 1
            nextQ = []


            if (depth == 1):
                while(q):
                    curr = q.pop(0)
                    if (curr.left):
                        tmp = curr.left
                        curr.left = TreeNode(val)
                        curr.left.left = tmp
                    else:
                        curr.left = TreeNode(val)

                    if (curr.right):
                        tmp = curr.right
                        curr.right = TreeNode(val)
                        curr.right.right = tmp
                    else:
                        curr.right = TreeNode(val)
            else:
                while(q):
                    curr = q.pop(0)
                    if (curr.left):
                        nextQ.append(curr.left)
                    if (curr.right):
                        nextQ.append(curr.right)
                q = nextQ
        return root

        
