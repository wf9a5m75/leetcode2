# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        result = tail = ListNode(-1)

        # Count up the length of the linked-list
        n = 0
        fast = head
        while(fast and fast.next):
            n += 2
            fast = fast.next.next
        if fast:
            n += 1

        # flipping grouped by k
        tmp = ListNode(0)
        for _ in range(n//k):
            nextTail = head
            for __ in range(k):
                tmpNext = tmp.next
                headNext = head.next
                tmp.next = head
                head.next = tmpNext
                head = headNext

            tail.next = tmp.next
            tmp.next = None
            tail = nextTail
        tail.next = head

        return result.next
