# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if (head is None):
            return None
        n = 0
        p = head
        while(p):
            p = p.next
            n += 1

        k = k % n
        if (k == 0):
            return head

        reverse = self.flipList(head)

        head = revR = reverse
        revL = ListNode(-1)
        tail = None
        for _ in range(k):
            revR = revR.next

            headNext = head.next
            currNext = revL.next
            revL.next = head
            head.next = currNext
            head = headNext


        revR = self.flipList(revR)

        tail = revL.next
        for _ in range(1, k):
            tail = tail.next

        tail.next = revR
        return revL.next



    def flipList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reverse = ListNode(-1)
        while(head):
            headNext = head.next
            head.next = reverse.next
            reverse.next = head
            head = headNext
        return reverse.next
