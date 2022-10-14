# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return None
        fast = head.next
        slow = head

        prevS = None
        while(fast):
            fast = fast.next
            if (fast):
                fast = fast.next
            prevS = slow
            slow = slow.next

        prevS.next = slow.next
        return head
