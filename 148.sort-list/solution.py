# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head is None or head.next is None):
            return head

        fast = head.next
        slow = head
        while(fast and fast.next):
            fast = fast.next.next
            slow = slow.next

        R = slow.next
        slow.next = None
        L = self.sortList(head)
        R = self.sortList(R)
        return self.merge(L, R)

    def merge(self, L: Optional[ListNode], R: Optional[ListNode]) -> Optional[ListNode]:
        if (L is None) or (R is None):
            return L or R

        result = tail = ListNode(0)
        while(L and R):
            if (L.val < R.val):
                tail.next = L
                L = L.next

            else:
                tail.next = R
                R = R.next
            tail = tail.next
        tail.next = L or R

        return result.next
