# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if (k == 1):
            return head

        total = 0
        p = head
        while(p):
            p = p.next
            total += 1
            if (p):
                p = p.next
                total += 1

        # dummy
        result = tail = ListNode(-1)

        kCnt = total // k
        dummy = ListNode(-1)
        while(head) and (kCnt > 0):
            cnt = 0
            last = None
            while(head) and (cnt < k):
                headNext = head.next
                dummyNext = dummy.next
                dummy.next = head
                head.next = dummyNext

                head = headNext
                cnt += 1

            tail.next = dummy.next
            dummy.next = None

            while(tail.next):
                tail = tail.next

            kCnt -= 1

        tail.next = head
        return result.next
