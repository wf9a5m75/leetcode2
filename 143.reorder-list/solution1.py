# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if (head.next is None):
            return

        # find the middle of the linked list
        fast = head
        slow = head
        lastSlow = None
        while(fast and fast.next):
            fast = fast.next.next
            lastSlow = slow
            slow = slow.next

        lastSlow.next = None

        # Create a half-size linked list the right isde from the middle
        r = ListNode(-1)
        while(slow):
            slowN = slow.next
            rN = r.next
            r.next = slow
            slow.next = rN
            slow = slowN

        # Create the result
        r = r.next
        p = head
        lastR = r
        while(p and r):
            pN = p.next
            rN = r.next

            lastR = r
            p.next = r
            r.next = pN
            r = rN
            p = pN

        if (r):
            lastR.next = r
