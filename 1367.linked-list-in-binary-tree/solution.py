# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# https://leetcode.com/problems/linked-list-in-binary-tree/discuss/524881/Python-Recursive-Solution-O(N-%2B-L)-Time
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if head is None:
            return True

        if root is None:
            return False

        def helper(listHead: Optional[ListNode], curr: Optional[TreeNode]) -> bool:
            if listHead is None:
                return True

            if curr is None:
                return False

            result = False
            if curr.val == listHead.val:
                result = helper(listHead.next, curr.left)
                return result or helper(listHead.next, curr.right)
            else:
                return False


        return helper(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
