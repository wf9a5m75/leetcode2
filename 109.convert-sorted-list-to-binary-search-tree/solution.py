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

        slow = faster = head
        slowBuffer = []
        while(faster):
            slowBuffer.append(slow)

            slow = slow.next
            faster = faster.next
            if (faster):
                faster = faster.next
        slow = slowBuffer[-1]

        root = TreeNode(slow.val)
        if (len(slowBuffer) > 1):
            slowBuffer[-2].next = None
            root.left = self.sortedListToBST(head)

        root.right = self.sortedListToBST(slow.next)

        return root
