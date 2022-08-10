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
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if (head is None):
            return None
        if (head.next is None):
            return TreeNode(head.val)

        slow = head
        fast = head.next.next
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        root = TreeNode(mid.val)

        slow.next = None
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)
        return root
